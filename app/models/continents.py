from app import db
from base import BaseModel


class Continent(BaseModel):
    __tablename__ = 'ob_continents'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.Integer)
    name = db.Column(db.String(128))

    def __repr__(self):
        return self.code

    @property
    def serialize(self):
        return {
            'code': self.code,
            'name': self.name
        }

    @staticmethod
    def required_fields():
        return ['code', 'name']

    @staticmethod
    def get_columns():
        # In first iteration I use
        # Continent.__table__.columns.keys()
        # But I don't want all the columns, so I do it manually
        return ['code', 'name']
