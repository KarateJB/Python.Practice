# Flask config reference: http://flask.pocoo.org/docs/1.0/config/
# Flask-Sqlalchemy config reference: http://flask-sqlalchemy.pocoo.org/2.3/config/

POSTGRES_ENV_VARS_DEV = {
    'user': 'postgres',
    'pwd': '1qaz2wsx',
    'host': 'jblin',
    'port': '5432',
    'db': 'postgres',
}

POSTGRES_ENV_VARS_PRD = {
    # Set the new variables for production here
}

class BaseConfig(object):
    # Flask
    DEBUG = False
    TESTING = False
    SECRET_KEY = "12qwaszx"
    JSONIFY_MIMETYPE = "application/json"

    # Flask-Sqlalchemy
    SQLALCHEMY_DATABASE_URI = "postgresql://%(user)s:%(pwd)s@%(host)s:%(port)s/%(db)s" % POSTGRES_ENV_VARS_DEV
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(BaseConfig):
    DEBUG = True

class TestConfig(BaseConfig):
    TESTING = True

class PrdConfig(BaseConfig):
    # SQLALCHEMY_DATABASE_URI = "postgresql://%(user)s:%(password)s@%(host)s:%(port)s/%(db)s" % POSTGRES_ENV_VARS_PRD
    pass
