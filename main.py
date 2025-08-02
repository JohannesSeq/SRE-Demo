#Libraries declaration
from flask import Flask, jsonify, request, render_template


#Defining application name
app = Flask(__name__)

#Creating the function for the site index
@app.route("/")
def index():
    return render_template("index.html")


#Application excecution
if __name__ == "__main__":
    app.run(debug = True)
    