# server module
from flask import Flask

# instance
app = Flask(__name__)

def create_app(environment):
    # setting up the environment to the instance
    app.config.from_object(environment)
    # return instance
    return app
