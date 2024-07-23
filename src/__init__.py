# md-apicompany/src/__init__.py
import os

from flask import Flask
from src.config import config
from dotenv import load_dotenv

from src.modelo.declarative_base import db

# app constructor
def create_app(config_name):
    app = Flask(__name__)

    # set config
    config_name = os.getenv('FLASK_ENV', 'development')

    # load .env file
    if config_name == 'development':
        env_file = '.env'
    elif config_name == 'testing':
        env_file = '.env.test'
    elif config_name == 'production':
        env_file = '.env.prod'
    else:
        env_file = '.env'

    load_dotenv(env_file)

    # set configuration
    if config_name == 'development':
        app.config.from_object(config[config_name])
    elif config_name == 'testing':
        app.config.from_object(config[config_name])
    elif config_name == 'production':
        app.config.from_object(config[config_name])
    else:
        app.config.from_object(config['default'])

    # init db
    db.init_app(app)

    print(f'Using {config_name} config')

    return app
