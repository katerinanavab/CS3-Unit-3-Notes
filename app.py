from flask import Flask

app = Flask(__name__)

# Index route for web app
@app.route("/")
def index():
    return "Hello, world!"

if __name__ == "__main__": 
    app.run(host='0.0.0.0', port=9874)
    