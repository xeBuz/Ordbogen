from app import db
from base import BaseModel
from app.models.continents import Continent


class Country(BaseModel):
    __tablename__ = 'ob_countries'

    id = db.Column(db.Integer, primary_key=True)
    iso_code = db.Column(db.String(2))
    iso_code_long = db.Column(db.String(3))
    short_name = db.Column(db.String)
    formal_name = db.Column(db.String(128))
    denonym = db.Column(db.String(128))
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
    itu = db.Column(db.String(256))
    web = db.Column(db.String(256))
    gis = db.Column(db.String(256))
    statics = db.Column(db.String(256))
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
            'denonym': self.denonym,
            'country_code': self.country_code,
            'continental_code': self.continental_code,
            'continent': self.continent,
            'coordinates': self.coordinate,
            'elevation': self.elevation,
            'elevation_low': self.elevation_low,
            'area': self.area,
            'land': self.land,
            'fertility': self.fertility,
            'population': self.population,
            'population_urban': self.population_urban,
            'ITU': self.itu,
            'web': self.web,
            'GIS': self.gis,
            'statics': self.statics,
            'flag': self.flag,
            'government': self.government,
            'boundary_box': self.boundary_box,
            'currency': self.currency,
        }

