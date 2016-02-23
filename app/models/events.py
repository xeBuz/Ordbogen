from app import db
from app.models.countries import Country
from .base import BaseModel


class EventCategory(db.Model):
    __tablename__ = 'ob_events_category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(129))


class Event(BaseModel):
    __tablename__ = 'ob_events'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    description = db.Column(db.Text)
    datetime = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey(EventCategory.id))
    category = db.relation(EventCategory)
    country_id = db.Column(db.Integer, db.ForeignKey(Country.id))
    country = db.relation(Country)

    def __repr__(self):
        return self.title

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'datetime': self.datetime,
            'country': {
                'iso_code': self.country.iso_code,
                'name': self.country.short_name
            },
            'category': self.category.name
        }

    @staticmethod
    def required_fields():
        return ['title', 'country_id', 'category_id']

    @staticmethod
    def get_columns():
        # In first iteration I use
        # Continent.__table__.columns.keys()
        # But I don't want all the columns, so I do it manually
        return ['title', 'description', 'category_id', 'datetime', 'country_id']
