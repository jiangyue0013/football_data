from operator import ge

from flask import Blueprint, redirect, render_template

from football_data.extensions import db
from football_data.forms.auth import LoginForm, RegisterForm
from football_data.models import User


auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return render_template('football_data/index.html')
    return render_template('auth/register.html', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.validate_password(form.password.data):
            return render_template('auth/login_success.html')
        else:
            redirect('auth/login')
    return render_template('auth/login.html', form=form)
