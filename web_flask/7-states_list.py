#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State

#Create the Flask application
app = Flask(__name__)

#Define the teardown_appcontext method to close theSQLAlchemy session after each request
@app.teardown_appcontext
def teardown_db(exception):
    storage.close()

#Define the /state_list route
@app.route('state_list', strict_slashes=False)
def states_list():
    #Fetch all State objects from the DBStorage sorted byname(A->Z)
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda state: state.name)

    # Render the template with the list of states
    return render_template('states_list.html', states=sorted_states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
