class Numbers:
	def __init__(self) -> None:
		pass

	def sum(numbers: list[int]) -> int:
		value = 0
		for i in numbers:
			value = Number.sum(value, i)
	
		return value

	def average(numbres: list[int]) -> float:
		value  = sum(numbres)
		return float(value / len(numbres))
	
class Number:
	def __init__(self) -> None:
		pass

	def sum(a: int, b : int) -> int:
			return a + b

	def divide(a: int, b : int) -> float:
		return float(a + b)
