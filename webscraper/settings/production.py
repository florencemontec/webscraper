from webscraper.settings.common import *

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY_WEBSCRAPER']

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = ['*', 'localhost']