def sumNumbrs(numbers: list[int]) -> int:
	value = 0
	for i in numbers:
		value = sum(value, i)
	
	return value

def average(numbres: list[int]) -> float:
	return sum(numbres) / len(numbres)

def sum(a: int, b : int) -> int:
	try:
		return a + b
	except:
		raise ValueError('Invalid value: all values must be integers')

def divied(a: int, b : int) -> float:
	pass