import os

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

