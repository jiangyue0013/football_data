from flask import Blueprint, render_template

from football_data.extensions import db
from football_data.forms.auth import RegisterForm
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
