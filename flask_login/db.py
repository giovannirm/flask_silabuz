from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy() #Instancia que contiene la conexión a la BD
migrate = Migrate()