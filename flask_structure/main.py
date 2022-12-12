from app import create_app
from flask import render_template, redirect, url_for
from db import db
from forms import SalonForm, AlumnoForm
from app.models.salon import Salon
from app.models.alumno import Alumno

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/salones/crear', methods=['post', 'get'])
def crear_salones():
    salon_form = SalonForm()

    if salon_form.validate_on_submit():
        print(salon_form.nombre.data)
        print(salon_form.hora_entrada.data)

        salon = Salon(salon_form.nombre.data, salon_form.hora_entrada.data)
        db.session.add(salon)
        db.session.commit()
        return redirect(url_for('salones'))
    return render_template('salon/crear.html', data = salon_form)

@app.route('/salones')
def salones():
    salon = Salon.query.all()
    return render_template('salon/index.html', salones = salon)

@app.route('/alumnos/crear', methods=['post', 'get'])
def crear_alumnos():
    alumno_form = AlumnoForm()

    if alumno_form.validate_on_submit():
        alumno = Alumno(alumno_form.nombre.data, alumno_form.apellido.data, alumno_form.email.data, alumno_form.id_aula.data)
        db.session.add(alumno)
        db.session.commit()
        return redirect(url_for('alumnos'))
    return render_template('alumno/crear.html', data = alumno_form)

@app.route('/alumnos')
def alumnos():
    alumno = Alumno.query.all()
    return render_template('alumno/index.html', alumnos = alumno)

db.init_app(app)
with app.app_context():
    db.create_all()
    print('BD Conectada')

if __name__ == '__main__':
    app.run(debug=True)