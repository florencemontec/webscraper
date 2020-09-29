from webscraper.settings.common import *

SECRET_KEY = os.environ.get('SECRET_KEY_WEBSCRAPER')

DEBUG = os.environ.get('DEBUG_VALUE_WEBSCRAPER') == 'True'
# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = ['*', 'localhost']