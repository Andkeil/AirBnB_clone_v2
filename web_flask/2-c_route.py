#!/usr/bin/python3
"""
Script starting a Flask web app
"""
from flask import Flask


app = Flask(__name__)
"""
Route: /
"""


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def display_c(text):
    text = text.replace("_", " ")
    return 'C {}'.format(text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
