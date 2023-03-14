import fitz

from typing import List

filename: str = "pdfs/daes1.pdf"

with fitz.open(filename) as test_file:

	plain_text: str = test_file[0].get_text()

splitted_text: List[str] = plain_text.split("\n")

[print(f"{i} - {v}") for i, v in enumerate(splitted_text)]
