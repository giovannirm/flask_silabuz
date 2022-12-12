from db import db

class Salon(db.Model):
    # __tablename__ = 'salones' #Se le da un nombre especificado
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    nombre = db.Column(db.String(20))
    hora_entrada = db.Column(db.Time)
    alumnos = db.relationship('Alumno', backref='salon', lazy='dynamic')

    def __init__(self, aula, hora_entrada):
        self.nombre = aula
        self.hora_entrada = hora_entrada