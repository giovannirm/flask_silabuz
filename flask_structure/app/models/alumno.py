from db import db

class Alumno(db.Model):
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    email = db.Column(db.String(50))
    id_aula = db.Column(db.Integer, db.ForeignKey('salon.id'))
    
    def __init__(self, nombre, apellido, email, id_aula):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.id_aula = id_aula