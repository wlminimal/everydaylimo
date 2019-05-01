from .base import *
import environ

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

# Configure Django App for Heroku.
# import django_heroku
# django_heroku.settings(locals())

env = environ.Env()

ALLOWED_HOSTS = ['floating-mesa-82197.herokuapp.com', 'everydaylimola.com', 'www.everydaylimola.com'] 
SECRET_KEY = env('SECRET_KEY')