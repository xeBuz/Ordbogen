from abc import abstractmethod
from app import db


class BaseModel(db.Model):
    __abstract__ = True

    def __init__(self, **kwargs):
        columns = [m.key for m in self.__table__.columns]
        for key in kwargs.keys():
            if key in columns:
                self.__setattr__(key, kwargs[key])

    @abstractmethod
    def __repr__(self):
        return

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @property
    @abstractmethod
    def serialize(self):
        return
