# core-apiselection/src/config.py

import os

# get base directory
basedir = os.path.join(os.path.dirname(__file__), '')

# main config class
class Config:
    # Flask Config
    PROPAGATE_EXCEPTIONS = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# development config
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or     'sqlite:///' + os.path.join(basedir, 'db/cuentas_claras_services_dev.sqlite')
    if not os.environ.get('DEV_DATABASE_URL'):
        print('DEV_DATABASE_URL environment variable does not exist, you will be using in-memory storage.')
    else:
        print('DEV_DATABASE_URL: {0}'.format(os.environ.get('DEV_DATABASE_URL')))

# testing config
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'src/db/cuentas_claras_services_test.sqlite')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    if not os.environ.get('TEST_DATABASE_URL'):
        print('TEST_DATABASE_URL environment variable does not exist, you will be using in-memory storage.')
    else:
        print('TEST_DATABASE_URL: {0}'.format(os.environ.get('TEST_DATABASE_URL')))

# production config
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'src/db/cuentas_claras_services.sqlite')
    if not os.environ.get('DATABASE_URL'):
        print('DATABASE_URL environment variable does not exist, you will be using in-memory storage.')
    else:
        print('DATABASE_URL: {0}'.format(os.environ.get('DATABASE_URL')))

# dictionary of config classes
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
