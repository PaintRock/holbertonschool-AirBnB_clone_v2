#!/usr/bin/python3
"""we are fetching states from dbstorage"""
from flask import Flask, render_template
from models import storage
from models.state import State

# Create the Flask application
app = Flask(__name__)


""" Define the teardown_appcontext method to close the
SQLAlchemy session after each request """


@app.teardown_appcontext
def teardown_db(exception):
    """This defines the teardown"""
    storage.close()


# Define the /state_list route
@app.route('/state_list', strict_slashes=False)
def states_list():
    """Fetch all State objects from the DBStorage sorted by name (A->Z)"""
    states = storage.all(State)
    # Render the template with the list of states
    return render_template('7-states_list.html', states=states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
