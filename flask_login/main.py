from app import create_app
from db import db
from flask import Flask, render_template, redirect, flash, url_for
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from forms import LoginForm
from app.models.user import User, AnonymousUser
from app.models.post import Post
from app.models.role import Role, Permission
from app.decorator import admin_required, permission_required
import os

app = create_app()
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.anonymous_user = AnonymousUser

@login_manager.user_loader #si el usuario está logueado en cada vista que visita
def load_user(id):
    return User.query.get(int(id))

@app.route('/')
@login_required
def index():
    return render_template('indexCss.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated: #si no está autentificado
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        # https://stackoverflow.com/questions/30150626/flask-login-user-is-set-to-anonymous-after-login
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
            
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    
    return render_template('login.html', form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/admin')
@login_required
@admin_required
def for_admins_only():
    return "Para admins!"
    
@app.route('/moderate')
@login_required
@permission_required(Permission.MODERATE)
def for_moderators_only():
    return "Para comentarios de moderadores!"

@app.route("/insert")
def insert():
    u = User(username = "giovanni", email = "giovanni@gmail.com")
    u.set_password("123")
    db.session.add(u)
    db.session.commit()
    return "Insertado"

# db.init_app(app)
# migrate.init_app(app, db)
# with app.app_context():
#     db.create_all()
#     print('BD Conectada')

if __name__ == '__main__':
    app.run(debug = os.environ.get('FLASK_DEBUG'))