from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_moment import Moment

db = SQLAlchemy() #Instancia que contiene la conexión a la BD
migrate = Migrate()
moment = Moment()
    