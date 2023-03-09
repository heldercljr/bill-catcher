class Bill:

	def __init__(self, due_date: str, bar_code: str,  value: float) -> None:
		
		self.doc_type = "Generic Bill"
		self.due_date: str = due_date
		self.bar_code: str = bar_code
		self.value: float = value