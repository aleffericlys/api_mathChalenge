from flask import Flask, request, jsonify
from flask_cors import CORS

from src.library import sumNumbrs, average

App = Flask('mathChallenge')
App.config.from_object(__name__)
CORS(App)


@App.route('/sum', methods=['GET'])
def sum():
	try:
		data = request.get_json()
		return jsonify({"sum": sumNumbrs(data)})
	except Exception as e:
		return jsonify(['Invalid value: input must be a list of integer values', str(e)])

@App.route('/average', methods=['GET'])
def averageN():
	try:
		data = request.get_json()
		return jsonify({"average": average(data)})
	except Exception as e:
		return jsonify(['Invalid value: input must be a list of integer values', str(e)])


if __name__ == '__main__':
	App.run(debug=True, port=3000)