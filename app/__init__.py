import os
from flask import Flask
from . import main
app = Flask(__name__)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
