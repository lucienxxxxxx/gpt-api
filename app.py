import requests
from flask import Flask, request

from gptService import getModels, chat

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/getModels', methods=["GET"])
def get_models():
    return getModels(), 200


@app.route('/chat', methods=["POST"])
def get_chat():
    prompt = request.form.get("prompt")
    message = request.form.get("message")
    return chat(prompt=prompt, message=message), 200

@app.route('/chat', methods=["POST"])
def get_chat():
    prompt = request.form.get("prompt")
    message = request.form.get("message")
    return chat(prompt=prompt, message=message), 200


if __name__ == '__main__':
    app.run()
