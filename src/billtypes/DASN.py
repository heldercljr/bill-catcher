import json
import re

from typing import Dict, List

from src.utils import parse_value, check_or_create_path


class DASN:
	"""
	Documento de Arrecadação do Simples Nacional
	"""

	def __init__(self, data: List[str]):
		
		self.cnpj: str = data[2]
		self.value: float = parse_value(data[12])
		self.due_date: str = data[9]
		self.bar_code: str = "".join(data[62:66]).replace(" ", "")
		self.pix_string: str = data[-1]
		self.doc_type: str = "Documento de Arrecadação do Simples Nacional"
		
		composition: List[str] = data[data.index("Composição do Documento de Arrecadação") + 1:data.index("Totais"):1]
		composition = [composition[i-1] for i in range(1, len(composition)) if composition[i-1].isupper() or re.match(r'\d+(,\d{2})', composition[i])]
		composition: List[Dict[str, float]] = [{"denomination": composition[i], "value": parse_value(composition[i+1])} for i in range(0, len(composition), 2)]

		self.doc_comp = composition
	
	def to_json(self):

		filename: str = re.sub(r"[^\w\s]", "", f"dasn_{self.cnpj}_{self.due_date}")
		filepath: str = f"jsons/{filename}.json"

		check_or_create_path("jsons")

		with open(filepath, "wb") as json_file:

			json_file.write(json.dumps(vars(self), ensure_ascii=False).encode("utf-8"))
