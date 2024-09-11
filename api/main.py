from flask import Flask, request, jsonify
from flask_cors import CORS

from src.library import Numbers

App = Flask('mathChallenge')
App.config.from_object(__name__)
CORS(App)


@App.route('/sum', methods=['POST'])
def sum():
	
	"""
    Rota para somar uma lista de números.
    
    Endpoint:
    /sum
    
    Método:
    POST
    
    Parâmetros:
    - JSON no corpo da requisição com uma lista de números inteiros, por exemplo:
      {
        "data": [1, 2, 3, 4]
      }
    
    Retorno:
    - JSON com a soma dos números fornecidos:
      {
        "sum": 10
      }
	
	Resposta de Erro (400 Bad Request):
	  [
		"Invalid value: input must be a list of integer values",
		"unsupported operand type(s) for +: 'int' and 'str'"
	  ]
    """
	try:
		data = request.get_json().get('data')
		return jsonify({"sum": Numbers.sum(data)})
	except Exception as e:
		return jsonify(['Invalid value: input must be a list of integer values', str(e)]), 400

@App.route('/average', methods=['POST'])
def averageN():
	"""
    Rota para calcular a média de uma lista de números.
    
    Endpoint:
    /average
    
    Método:
    POST
    
    Parâmetros:
    - JSON no corpo da requisição com uma lista de números inteiros, por exemplo:
      {
        "data": [1, 2, 3, 4]
      }
    
    Retorno:
    - JSON com a média dos números fornecidos:
      {
        "average": 2.5
      }

	Resposta de Erro (400 Bad Request):
	  [
		"Invalid value: input must be a list of integer values",
		"unsupported operand type(s) for +: 'int' and 'str'"
	  ]
    """
	try:
		data = request.get_json().get('data')
		print(data)
		return jsonify({"average": Numbers.average(data)})
	except Exception as e:
		return jsonify(['Invalid value: input must be a list of integer values', str(e)]), 400


if __name__ == '__main__':
	App.run(debug=True, port=3000)