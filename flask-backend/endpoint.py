from flask import Flask

app = Flask(__name__)


@app.route("/")
def recieve_points():
    return "Hello World !"

app.run()
