#!/usr/bin/python3
"""
Script starting a Flask web app
"""
from flask import render_template
from models import storage
from flask import Flask
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """
    closes storage
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_state():
    states = storage.all("State").values()
    city_state = []
    for state in sorted(states, key=lambda k: ;.name):
        city_state.append([state, state.cities])
    return render_template('8-cities_by_states.html', city_state = city_state

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
