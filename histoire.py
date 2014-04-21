from flask import Flask
app = Flask(__name__)

# import json

from model import (
    session as db_session,
    # User,
)

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/pins", methods=['POST'])
def create_pin():
    pass


@app.route("/pins", methods=['GET'])
def get_pins():
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
