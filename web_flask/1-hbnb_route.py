#!usr/bin/python3
""" 1-Starts a Flask web application """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """say hello"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """show HBNB"""
    return 'HBNB'


if __name__ == '__main__':
    """run host"""
    app.run(host='0.0.0.0', port=5000)
