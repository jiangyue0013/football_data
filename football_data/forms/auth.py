from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Length, EqualTo

from football_data.models import User

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 30)])
    password = PasswordField('Password', validators=[DataRequired(), Length(8-128), EqualTo('password2')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField()

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('The username is already in use.')