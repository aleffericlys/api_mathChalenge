from flask import Flask, request, jsonify
from flask_cors import CORS
import json

from src.library import sumNumbrs, average

App = Flask('mathChallenge')
App.config.from_object(__name__)
CORS(App)

@App.route('/', methods=['GET'])
def mainroute():
	return jsonify('Hello World')


@App.route('/averageteste', methods=['GET'])
def sumteste():
	try:
		data = request.get_json()
		return jsonify(average(data))
	except Exception as e:
		return jsonify(['Invalid value: input must be a list of integer values', str(e)])


if __name__ == '__main__':
	App.run(debug=True, port=3000)