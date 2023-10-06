# flask --app hello run

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route('/post', methods=['POST'])
def post():
    post_body = request.get_json()
    print(post_body)
    return jsonify({"status": "success", "message": 3}), 201

