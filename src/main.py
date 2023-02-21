#!/usr/bin/env python
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("home.html")


@app.route("/<name>")
def greetings(name):
    return f"Welcome {name}!"


@app.route("/square/<int:number>")
def show_square(number):
    return f"Square of {number} is {number * number}"


if __name__ == "__main__":
    app.run(debug=True, port=8080)
