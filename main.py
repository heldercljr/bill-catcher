import fitz
import re

from pathlib import Path
from typing import List

from src.billtypes import DASN
from src.billtypes import DAES


def main() -> None:

	DOCUMENT_TYPES = ("DASN", "DAES")

	for filepath in Path("pdfs").glob("*.pdf"):

		if filepath.stem.upper().startswith(DOCUMENT_TYPES):
		
			DOC = globals()[filepath.stem[:4].upper()]

			filename = filepath.absolute()

			with fitz.open(filename) as bill:

				plain_text: str = bill[0].get_text()

				splitted_text: List[str] = plain_text.split("\n")

				DOC(splitted_text).to_json()


if __name__ == "__main__":
	main()
