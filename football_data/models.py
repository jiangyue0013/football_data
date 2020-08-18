from flask_sqlalchemy import model
from football_data.extensions import db
from werkzeug.security import check_password_hash, generate_password_hash


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), nullable=False)
    _password_hash = db.Column(db.String(128))

    @property
    def password(self):
        return self._password_hash
    
    def set_password(self, password):
        self._password_hash = generate_password_hash(password)
    
    def validate_password(self, password):
        return check_password_hash(self._password_hash, password)
