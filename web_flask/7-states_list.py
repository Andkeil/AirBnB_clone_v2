#!/usr/bin/python3
"""
Script starting a Flask web app
"""
from flask import render_template
from models import storage
from flask import Flask


app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """
    closes storage
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list():
    state_list = storage.all("State")
    state_array = state_list.values()
    sort_arr = []
    for state in sorted(state_array, key=lambda k: k.name):
        sort_arr.append(state)
    return render_template('7-states_list.html', state_lists=sort_arr)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
