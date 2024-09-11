class Numbers:
	"""
    	Classe que contém métodos estáticos para operações com listas de números.
    """
	@staticmethod
	def sum(numbers: list[int]) -> int:
		"""
			Calcula a soma de todos os números em uma lista.

			Args:
				numbers (list[int]): Lista de números inteiros.

			Returns:
				int: A soma de todos os números da lista.
        """

		value = 0
		for i in numbers:
			value = Number.sum(value, i)
	
		return value
	
	@staticmethod
	def average(numbres: list[int]) -> float:
		"""
			Calcula a média de todos os números em uma lista.

			Args:
				numbers (list[int]): Lista de números inteiros.

			Returns:
				float: A média dos números da lista.
        """
		value  = sum(numbres)
		return Number.divide(value, len(numbres))
	
class Number:
	"""
    	Classe que contém métodos estáticos para operações com números individuais.
    """
	@staticmethod
	def sum(a: int, b : int) -> int:
		"""
			Calcula a soma de dois números inteiros.

			Args:
				a (int): O primeiro número.
				b (int): O segundo número.

			Returns:
				int: A soma de `a` e `b`.
        """	
		return a + b
	
	@staticmethod
	def divide(a: int, b : int) -> float:
		"""
			Divide dois números inteiros e retorna o resultado como um número de ponto flutuante.

			Args:
				a (int): O dividendo.
				b (int): O divisor.

			Returns:
				float: O resultado da divisão `a / b`.

			Raises:
				ZeroDivisionError: Se `b` for zero.
        """
		return float(a / b)
