from typing import Any, Dict
from json import dumps


class Report:

	def __init__(self, source: Dict[str, Any]) -> None:
		self.__dict__.update(source)
	

	def __str__(self) -> str:
		return ", ".join(f"{k} = {v!r}" for k, v in self.__dict__.items())
	

	def __repr__(self) -> str:

		attributes = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())

		return f"{self.__class__.__name__}({atributos})"