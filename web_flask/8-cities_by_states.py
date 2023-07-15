#!/usr/bin/python3
"""Cities by state using a flask and probably jinja"""
from flask import Flask, render_template, request, jsonify
from flask import Flask
from models.state import State
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception=None):
    """Closes the database session after each request."""
    storage.close()


def load_cities_by_states():
    """Load all cities of a state from the storage engine."""
    if storage.__class__.__name__ == 'DBStorage':
        states = sorted(storage.all("State").values(), key=lambda x: x.name)
    else:
        states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    cities_by_states = {}
    for state in states:
        if storage.__class__.__name__ == 'DBStorage':
            cities = sorted([city for city in state.cities], key=lambda x: x.name)
        else:
            cities = sorted(list(state.cities), key=lambda x: x.name)
        cities_by_states[state.id] = {
            'state': state.name,
            'cities': [{'id': city.id, 'name': city.name} for city in cities]
        }
    return cities_by_states


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Render the HTML page displaying cities by states."""
    cities_data = load_cities_by_states()
    return render_template('8-cities_by_states.html', cities_data=cities_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
