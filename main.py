#Libraries declaration
from flask import Flask
from flask import jsonify
from flask import request

#Defining application name
app = Flask(__name__)

#Creating the function for the site index
@app.route("/")
def index():
    return "Hello!"


#Application excecution
if __name__ == "__main__":
    app.run(debug = True)