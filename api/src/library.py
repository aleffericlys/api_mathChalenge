class Numbers:

	def sum(numbers: list[int]) -> int:
		value = 0
		for i in numbers:
			value = Number.sum(value, i)
	
		return value

	def average(numbres: list[int]) -> float:
		value  = sum(numbres)
		return Number.divide(value, len(numbres))
	
class Number:

	def sum(a: int, b : int) -> int:
			return a + b

	def divide(a: int, b : int) -> float:
		return float(a / b)
