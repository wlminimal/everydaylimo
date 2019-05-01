from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

# Configure Django App for Heroku.
# import django_heroku
# django_heroku.settings(locals())

ALLOWED_HOSTS = ['floating-mesa-82197.herokuapp.com'] 