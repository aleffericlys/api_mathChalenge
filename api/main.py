from flask import Flask, jsonify
from flask_cors import CORS
import json

from src.library import sumNumbrs, average

App = Flask('mathChallenge')
App.config.from_object(__name__)
CORS(App)

@App.route('/', methods=['GET'])
def mainroute():
	return jsonify('Hello World')


@App.route('/sumteste', methods=['GET'])
def sumteste():
	list = [1, 2, 3, 4, 540]
	return jsonify(sumNumbrs(list))


if __name__ == '__main__':
	App.run(debug=True, port=3000)
	# sumteste()