# chat2openapi API endpoints definitions
import flask
from flask import Flask, request, jsonify

app = Flask(__name__)

`@app.route('/', methods=['GET'])
def hello_api():
    return jsonify({'message': 'Hello, World!'})
