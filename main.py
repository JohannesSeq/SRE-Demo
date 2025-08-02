#Libraries declaration
from flask import Flask
from flask import jsonify
from flask import request

@app.route("/")
def index():
    return "Hello!"

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug = True)