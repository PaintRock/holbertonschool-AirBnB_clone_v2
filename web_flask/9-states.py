#!/usr/bin/python3
"""doc this"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception=None):
    """Closes the database session after each request."""
    storage.close()


@app.route('/states', strict_slashes=False)
def states_list():
    """Render the HTML page displaying the list of states."""
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    return render_template(\
        'states_and_cities.html', states=states, cities=None)


@app.route('/states/<id>', strict_slashes=False)
def cities_list(id):
    """Render the HTML page displaying cities for a specific state."""
    state = storage.get(State, id)
    if state is None:
        return render_template('states_and_cities.html', states=None,
        cities=None)

    cities = sorted(state.cities, key=lambda x: x.name)
    return render_template('states_and_cities.html', states=None,
        cities=cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
