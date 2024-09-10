def sumNumbrs(numbers: list[int]) -> int:
	value = 0
	for i in numbers:
		value = sum(value, i)
	
	return value

def average(numbres: list[int]) -> float:
	value  = sumNumbrs(numbres)
	return float(value / len(numbres))
	

def sum(a: int, b : int) -> int:
		return a + b

def divide(a: int, b : int) -> float:
	return float(a + b)
	