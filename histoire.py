from flask import Flask
app = Flask(__name__)

# import json

from model import (
    session as db_session,
    User,
    Book,
    Location,
)

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/pins", methods=['POST'])
def create_pin():
    '''
    This function adds a pin to the map.
    If there's a logged in user, the pin should be readily approved and added.
    If there's not a logged in user, the pin should be sent to admin for approval.
    '''
    pass


@app.route("/pins", methods=['GET'])
def get_pins():
    # TODO: split this function out to get historical and
    # historical fiction pins seperately.
    pass


@app.route("/pins/id", methods=['PUT'])
def update_pin():
    pass


@app.route("/pins/id", methods=['GET'])
def get_pin():
    pass


@app.route("/pins/id", methods=['DELETE'])
def delete_pin():
    pass

if __name__ == "__main__":
    app.run(debug=True)
