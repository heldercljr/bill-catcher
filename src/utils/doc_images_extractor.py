import fitz

filename: str = "pdfs/dasn2.pdf"

with fitz.open(filename) as pdf:

	images = pdf.get_page_images(0)

	for image in images:

		width = image[2]
		height = image[3]

		if width == 350 and height == 350:
			xref = image[0]

	picture = fitz.Pixmap(pdf, xref)
	picture = fitz.Pixmap(fitz.csRGB, picture)

	image_data = picture.tobytes()

	with open(f"{xref}_image.png", "wb") as image_file:

			image_file.write(image_data)
