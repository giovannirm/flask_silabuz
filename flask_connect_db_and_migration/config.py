import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'esta-es-una-clave-secreta'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/db_flask_connect_db_and_migration'
    SQLALCHEMY_TRACK_MODIFICATIONS = False