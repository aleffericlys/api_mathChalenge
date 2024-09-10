from flask import Flask, jsonify
from flask_cors import CORS
import json


App = Flask('mathChallenge')
App.config.from_object(__name__)
CORS(App)

@App.route('/', methods=['GET'])
def mainroute():
	return jsonify('Hello World')




if __name__ == '__main__':
	App.run(debug=True, port=3000)