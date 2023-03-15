import json
import re

from typing import Dict, List

from src.utils import parse_value, check_or_create_path


class DAES:
	"""
	Documento de Arrecadação do eSocial
	"""
	
	def __init__(self, data: List[str]):

		self.cpf: str = data[2]
		self.value: float = parse_value(data[14])
		self.due_date: str = data[11]
		self.bar_code: str = "".join(data[57:61]).replace(" ", "")
		self.pix_string: str = data[-1]
		self.doc_type: str = "Documento de Arrecadação do eSocial"

		composition: List[str] = data[data.index("Composição do Documento de Arrecadação") + 1:data.index("Totais"):1]
		composition = [composition[i-1] for i in range(1, len(composition)) if composition[i-1].isupper() or re.match(r'\d+(,\d{2})', composition[i])]
		composition = [elem for elem in composition if not elem.startswith(" ")]
		composition: List[Dict[str, float]] = [{"denomination": composition[i], "value": parse_value(composition[i+1])} for i in range(0, len(composition), 2)]
		
		self.doc_comp: List[Dict[str, float]] = composition

	def to_json(self):

		filename: str = re.sub(r"[^\w\s]", "", f"daes_{self.cpf}_{self.due_date}")
		filepath: str = f"jsons/{filename}.json"

		check_or_create_path("jsons")
		
		with open(filepath, "wb") as json_file:

			json_file.write(json.dumps(vars(self), ensure_ascii=False).encode("utf-8"))
