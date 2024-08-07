# my imports
from .base import *
from mysite.env import env

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', default=True)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=['localhost', '0.0.0.0', '127.0.0.1'])