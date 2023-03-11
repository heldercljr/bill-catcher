import os

def parse_value(value: str) -> float:
	return float(value.replace(",", "."))

def check_or_create_path(path: str) -> bool:
	if not os.path.exists(path):
		os.makedirs(path)
