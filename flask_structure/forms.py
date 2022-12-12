
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, EmailField, TimeField, IntegerField
from wtforms.validators import DataRequired

class SalonForm(FlaskForm):
    nombre = StringField('Nombre del salón: ', validators=[DataRequired()])
    hora_entrada = TimeField('Hora de entrada: ', validators=[DataRequired()])
    boton = SubmitField('Registrar Salón')

class AlumnoForm(FlaskForm):
    nombre = StringField('Nombre: ', validators=[DataRequired()])
    apellido = StringField('Apellido: ', validators=[DataRequired()])
    email = EmailField('Email: ', validators=[DataRequired()])
    id_aula = IntegerField('ID de aula: ', validators=[DataRequired()])
    boton = SubmitField('Registrar Alumno')