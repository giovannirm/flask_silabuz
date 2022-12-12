from flask import Flask, render_template, redirect, url_for, flash
from models import LoginForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    info = 'Hola mundo desde Flask con el método'
    return render_template('index.html', data = info)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Inicio de sesión solicitado por {}, ¿Recordar?={}'.format(form.username.data, form.remember_me.data))
        return redirect('/css')

    return render_template('login.html', form = form)

@app.route('/css')
def index_css():
    return render_template('indexCss.html')

# if __name__ == '__main__':
#     app.run(debug=True)