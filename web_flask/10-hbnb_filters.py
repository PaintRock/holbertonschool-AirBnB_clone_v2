#!/usr/bin/python3
"""Ptut it all together and watch it not work"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception=None):
    """Closes the database session after each request."""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Render the HTML page with filters for states, cities, and amenities."""
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    cities = sorted(storage.all(City).values(), key=lambda x: x.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda x: x.name)
    return render_template('10-hbnb_filters.html', states=states, cities=cities, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
