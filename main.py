#Libraries declaration
from flask import Flask, jsonify, request, render_template, redirect, url_for
import os
import datetime


#Defining application name
app = Flask(__name__)

#Logging enable
logging = True

def logging():
    LogName = "Verbose_" + ""
    Log = open(,"x")

#Creating the function for the site index
@app.route("/")
def index():
    return render_template("index.html")

#Creating the function for the first monitorization site
@app.route("/monitoring1")
def mon1():
    return render_template("monitoring1.html")

#Creating the function for the first monitorization site
@app.route("/monitoring2")
def mon2():
    return "monitoring site 2!"

#Creating the function for the first monitorization site
@app.route("/alerts")
def alerts():
    return "Alerts site!"

#Creating the function for the first monitorization site
@app.route("/incidents")
def incidents():
    return "incidents site!"

#Application excecution
if __name__ == "__main__":
    #Settings to run the application publicly
    port = int(os.environ.get('PORT', 7575))
    app.run(host='0.0.0.0', port=port)
    
    #SSL Configurations to enable HTTPS
    app.run(ssl_context='adhoc')
    #pip install pyopenssl -- to install openssl and use certificates

    #Start running the application
    app.run(debug = True)
