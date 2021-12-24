from flask import Flask, jsonify, request
from Data import Data

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "Data":Data,
        "message":'success'
    },200)

if __name__ == '__main__':
    app.run()