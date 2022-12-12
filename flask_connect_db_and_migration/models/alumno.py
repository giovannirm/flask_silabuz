from app import db

class Alumno(db.Model):
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    idAula = db.Column(db.Integer, db.ForeignKey('salon.id'))