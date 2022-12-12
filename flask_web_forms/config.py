import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'esta-es-una-clave-secreta'