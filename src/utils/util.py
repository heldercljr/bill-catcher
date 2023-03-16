import os
import imaplib
import email

from typing import List

from cv2 import imread, imdecode, QRCodeDetector, IMREAD_COLOR
from fitz import Document, Pixmap, csRGB
from numpy import frombuffer, uint8

def parse_value(value: str) -> float:
	return float(value.replace(",", "."))

def check_or_create_path(path: str) -> bool:
	if not os.path.exists(path):
		os.makedirs(path)

def pix_qrcode_decoder(doc: Document) -> str:

	images: List = doc.get_page_images(0)

	for image in images:

		width: int = image[2]
		height: int = image[3]

		if width == 350 and height == 350:
			xref = image[0]

	picture: Pixmap = Pixmap(doc, xref)
	picture: Pixmap = Pixmap(csRGB, picture)

	image_raw_data: bytes = picture.tobytes()
	image_data = imdecode(frombuffer(image_raw_data, uint8), IMREAD_COLOR)

	pix_string: str = QRCodeDetector().detectAndDecode(image_data)[0]

	return pix_string

def email_catcher() -> None:
	#Conectando ao servidor do outlook com IMAP
	objCon = imaplib.IMAP4_SSL("imap.outlook.com")

	#Credenciais
	login = "billteste165@outlook.com"
	senha = "@teste123"

	objCon.login(login, senha)

	#Loopar a caixa de entrada
	objCon.select(mailbox='inbox', readonly=True)
	respostas, idDosEmails = objCon.search(None, 'All')

	for num in idDosEmails[0].split():
		#decodificando o email e jogando em uma variavel as partes
		resultado, dados = objCon.fetch(num, '(RFC822)')
		texto_do_email = dados[0][1]
		texto_do_email = texto_do_email.decode('utf-8')
		texto_do_email = email.message_from_string(texto_do_email)

		for part in texto_do_email.walk():
			if part.get_content_maintype() == 'multipart':
				continue
			if part.get('Content-Disposition') is None:
				continue
			#Pegando o nome do arquivo em anexo
			fileName = os.path.dirname(os.path.abspath('__file__')) + f"/pdfs/" + part.get_filename()

			#Criamos um arquivo com o mesmo nome na pasta local
			arquivo = open(fileName, 'wb')

			#Escrevendo o binário do anexo no arquivo
			arquivo.write(part.get_payload(decode=True))
			arquivo.close()


