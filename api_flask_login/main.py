from app import create_app
from db import db
from flask import Flask, render_template, redirect, flash, url_for, Blueprint
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from forms import LoginForm, EditProfileForm, PostForm
from app.models.user import User, AnonymousUser
from app.models.post import Post
from app.models.role import Role, Permission
from app.decorator import admin_required, permission_required
import os
import hashlib

app = create_app()
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.anonymous_user = AnonymousUser

@login_manager.user_loader #si el usuario está logueado en cada vista que visita
def load_user(id):
    return User.query.get(int(id))

# @app.route('/')
# @login_required
# def index():
#     return render_template('indexCss.html')

@app.route('/', methods = ['GET', 'POST'])
@login_required
def index():
    # Añadimos los post
    form = PostForm()
    if current_user.can(Permission.WRITE) and form.validate_on_submit():
        post = Post(body=form.body.data, author=current_user._get_current_object())
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('index'))
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template("index.html", form = form, posts = posts, WRITE = Permission.WRITE)

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
    
    return render_template('login.html', form=form)

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

def gravatar(email="hola@gmail.com", size=100, default="identicon", rating="g"):
    url = "https://secure.gravatar.com/avatar"
    hash = hashlib.md5(email.encode("utf-8")).hexdigest()
    return "{url}/{hash}?s={size}&d={default}&r={rating}".format(
        url=url, hash=hash, size=size, default=default, rating=rating
    )

@app.route("/")
def dibujar():
    avt = gravatar(size=256)
    return render_template("avatar.html", avatar=avt)

@app.route('/usuario/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)

@app.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user._get_current_object())
        db.session.commit()
        flash('Tu perfil se actualizó correctamente.')
        return redirect(url_for('.user', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit-profile.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug = os.environ.get('FLASK_DEBUG'))