import time
from app import db, app
from datetime import datetime, timedelta
from werkzeug.security import gen_salt
from app.models.users import Users
from .base import BaseModel


def generate_key():
    return gen_salt(60)


def generate_expiration():
    expiration = datetime.now() + timedelta(hours=app.config['TOKEN_TTL_HOURS'])
    return expiration.strftime('%s')


class Tokens(BaseModel):
    __tablename__ = 'ob_tokens'

    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(60), default=generate_key())
    user_id = db.Column(db.Integer(), db.ForeignKey(Users.id))
    user = db.relation(Users)
    expiration = db.Column(db.Integer, default=generate_expiration())

    def __repr__(self):
        return self.key

    @property
    def serialize(self):
        """
        Serialize the Model for the JSON responses

        :return:
        """
        return {
            'access_key': self.key,
            'expiration': self.readable_expiration,
            'user': {
                'name': self.user.name,
                'e-mail': self.user.mail
            }
        }

    @property
    def readable_expiration(self):
        """
        Convert the timestamp in a human readable value

        :return:
        """
        value = datetime.fromtimestamp(self.expiration)
        return value.strftime('%Y-%m-%d %H:%M:%S')

    def expired(self):
        """
        Validate if the current time is greater than the expiration date. If the time is greater, the token has expired
        :return:
        """
        now = time.time()
        if float(now) > float(self.expiration):
            self.delete()
            return True
        else:
            return False
