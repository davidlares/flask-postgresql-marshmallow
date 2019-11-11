# server module
from flask import Flask
# instance
app = Flask(__name__)

def create_app():
    # return instance
    return app
