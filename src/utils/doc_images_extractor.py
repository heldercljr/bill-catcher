import fitz

filename: str = "pdfs/daes1.pdf"

with fitz.open(filename) as pdf:

	imagens = pdf.get_page_images(0)

	for imagem in imagens:

		xref = imagem[0]
		smask = imagem[1]

		width = imagem[2]
		height = imagem[3]

		print(xref, smask, width, height)

		pix = fitz.Pixmap(pdf, xref)

		imgdata = pix.tobytes("png")

		with open(f"{xref}_image.png", "wb") as img_file:

			img_file.write(imgdata)