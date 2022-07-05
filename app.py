from flask import Flask
import os
import importlib
from dotenv import load_dotenv

def app(test_config=None):
    application = Flask(__name__, instance_relative_config=True)
    if test_config is None:
        application.config.from_mapping(
            SECRET_KEY='dev'
        )
    else:
        application.config.from_mapping(test_config)

    return application


application = app()

load_dotenv()

import src
