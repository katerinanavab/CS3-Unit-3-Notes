from flask import Flask
from flask import render_template

app = Flask(__name__)

# Index route for web app
@app.route("/")
def index():
    return "Hello, world!"


@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name_data = None):
    return render_template("hello_there.html", name=name_data)