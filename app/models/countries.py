from app import db
from app.models.continents import Continent
from .base import BaseModel


class Country(BaseModel):
    __tablename__ = 'ob_countries'

    id = db.Column(db.Integer, primary_key=True)
    iso_code = db.Column(db.String(2))
    iso_code_long = db.Column(db.String(3))
    short_name = db.Column(db.String)
    formal_name = db.Column(db.String(128))
    demonym = db.Column(db.String(128))
    country_code = db.Column(db.Integer)
    continental_code = db.Column(db.Integer, db.ForeignKey(Continent.code))
    continent = db.relation(Continent)
    coordinates = db.Column(db.String(128))
    elevation = db.Column(db.Integer)
    elevation_low = db.Column(db.Integer)
    area = db.Column(db.Integer)
    land = db.Column(db.Integer)
    fertility = db.Column(db.Float)
    population = db.Column(db.Integer)
    population_urban = db.Column(db.Integer)
    birth = db.Column(db.Float)
    death = db.Column(db.Float)
    itu = db.Column(db.String(256))
    web = db.Column(db.String(256))
    gis = db.Column(db.String(256))
    statistics = db.Column(db.String(256))
    flag = db.Column(db.String(256))
    government = db.Column(db.String(128))
    boundary_box = db.Column(db.String(128))
    currency = db.Column(db.String(64))

    def __repr__(self):
        return self.iso_code

    @property
    def serialize(self):
        return {
            'iso_code': self.iso_code,
            'iso_code_long': self.iso_code_long,
            'short_name': self.short_name,
            'formal_name': self.formal_name,
            'demonym': self.demonym,
            'country_code': self.country_code,
            'continental_code': self.continental_code,
            'coordinates': self.coordinates,
            'elevation': self.elevation,
            'elevation_low': self.elevation_low,
            'area': self.area,
            'land': self.land,
            'fertility': self.fertility,
            'population': self.population,
            'population_urban': self.population_urban,
            'birth': self.birth,
            'death': self.death,
            'ITU': self.itu,
            'web': self.web,
            'GIS': self.gis,
            'statistics': self.statistics,
            'flag': self.flag,
            'government': self.government,
            'boundary_box': self.boundary_box,
            'currency': self.currency,
        }

    @staticmethod
    def required_fields():
        return ['iso_code', 'iso_code_long', 'short_name', 'continental_code', 'country_code']

    @staticmethod
    def get_columns():
        # In first iteration I use
        # Continent.__table__.columns.keys()
        # But I don't want all the columns, so I do it manually

        return ['iso_code', 'iso_code_long', 'short_name', 'formal_name', 'demonym', 'country_code', 'continental_code',
                'coordinates', 'elevation', 'elevation_low', 'area', 'land', 'fertility', 'population',
                'population_urban', 'birth', 'death', 'itu', 'web', 'gis', 'statistics', 'flag', 'government',
                'boundary_box', 'currency']
