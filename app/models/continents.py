from app import db


class Continent(db.Model):
    __tablename__ = 'ob_continents'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.Integer)
    name = db.Column(db.String(128))

    def __init__(self, code, name):
        self.code = code
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @property
    def serialize(self):
        return {
            'code': self.code,
            'name': self.name
        }

    def __repr__(self):
        return self.code
