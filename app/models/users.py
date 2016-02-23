from app import db
from .base import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash


class Users(BaseModel):
    __tablename__ = 'ob_users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    password = db.Column(db.String(128))

    def __repr__(self):
        return self.name

    def __init__(self, **kwargs):
        if kwargs['password']:
            kwargs['password'] = generate_password_hash(kwargs['password'])

        super(BaseModel, self).__init__(**kwargs)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'e-mail': self.email,
        }

    @staticmethod
    def required_fields():
        return ['name', 'email', 'password']

    @staticmethod
    def get_columns():
        return ['name', 'email', 'password']

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)





