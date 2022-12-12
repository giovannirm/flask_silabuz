from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from app.config import Config

def create_app(): #función de fábrica
    app = Flask(__name__)
    app.config.from_object(Config)

    Bootstrap(app)
    SQLAlchemy(app)
    return app