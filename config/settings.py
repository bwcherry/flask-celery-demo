from os import environ
from distutils.util import strtobool

# Whether debug mode is enabled.
# When using flask run to start the development server,
# an interactive debugger will be shown for unhandled exceptions,
# and the server will be reloaded when code changes. 
FLASK_DEBUG = strtobool(environ['FLASK_DEBUG'])

# Generate a nice key using the command below
#   python -c 'import secrets; print(secrets.token_hex())'
SECRET_KEY = environ['SECRET_KEY']

# Configure the SQLite database, relative to the app instance folder
SQLALCHEMY_DATABASE_URI = environ['SQLALCHEMY_DATABASE_URI']

# Variables for Celery
CELERY_CONFIG = {
    'broker_url': environ['CELERY_BROKER_URL'],
    'result_backend': environ['CELERY_RESULT_BACKEND'],
}

# I know that you could provide a fallback for these values,
# but I took the approach that it would be better to get a key error
# so you know that your configuration settings were not getting loaded.
