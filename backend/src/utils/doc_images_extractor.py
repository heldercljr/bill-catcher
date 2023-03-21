import cv2
import numpy

from typing import List

from cv2 import imread, imdecode, QRCodeDetector, IMREAD_COLOR
from fitz import Document, Pixmap, csRGB, open as doc_open
from numpy import frombuffer, uint8

from util import check_or_create_path

filename: str = "pdfs/daes1.pdf"

with doc_open(filename) as pdf:

	images: List = pdf.get_page_images(0)

	for image in images:

		width: int = image[2]
		height: int = image[3]

		if width == 350 and height == 350:
			xref: int = image[0]

	picture: Pixmap = Pixmap(pdf, xref)
	picture: Pixmap = Pixmap(csRGB, picture)

image_raw_data: bytes = picture.tobytes()
image_data = imdecode(numpy.frombuffer(image_raw_data, numpy.uint8), IMREAD_COLOR)

data: str = QRCodeDetector().detectAndDecode(image_data)[0]

print(data)
