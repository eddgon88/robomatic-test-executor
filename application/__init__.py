# application/__init__.py
import config
import os
from flask import Flask


def create_app():
    app = Flask(__name__)
    environment_configuration = os.environ['CONFIGURATION_SETUP']
    app.config.from_object(environment_configuration)

    with app.app_context():
        from .test_executor import test_executor_blueprint
        app.register_blueprint(test_executor_blueprint)
        return app
