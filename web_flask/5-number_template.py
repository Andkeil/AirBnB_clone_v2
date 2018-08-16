#!/usr/bin/python3
"""
Script starting a Flask web app
"""
from flask import render_template
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


@app.route('/python', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def display_py(text="is cool"):
    return("Python {}".format(text.replace("_", " ")))


@app.route('/number/<int:num>', strict_slashes=False)
def display_num(num):
    return "{} is a number".format(num)


@app.route('/number_template/<int:num>', strict_slashes=False)
def display_numtmp(num):
    return render_template('5-number.html', num=num)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
