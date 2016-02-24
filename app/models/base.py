from abc import abstractmethod
from app import db


class BaseModel(db.Model):
    __abstract__ = True

    def __init__(self, **kwargs):
        """
        Initialize the BaseModel. This method will receive a unknown list with key=value elements
        From that list, will use just the key matching with a column name in the table.

        :param kwargs:
        """
        columns = [m.key for m in self.__table__.columns]
        for key in kwargs.keys():
            if key in columns:
                self.__setattr__(key, kwargs[key])

    @abstractmethod
    def __repr__(self):
        return

    @staticmethod
    def required_fields():
        """
        Required fields

        :return:
        """
        return None

    @staticmethod
    def model_fields():
        """
        Usable field list from the model, because not all the fields should be modified

        :return:
        """
        return None

    def save(self):
        """
        Add the object to the transaction and commit the session
        """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """
        Remove the object from the transaction and commit the session
        """
        db.session.delete(self)
        db.session.commit()

