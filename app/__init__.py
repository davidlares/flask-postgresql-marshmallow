# server module
from flask import Flask
from .models import db
from .models.task import Task

# instance
app = Flask(__name__)

def create_app(environment):
    # setting up the environment to the instance
    app.config.from_object(environment)

    # app context
    with app.app_context():
        # initialize app
        db.init_app(app)
        # create all models (table)
        db.create_all()

    # return instance
    return app
