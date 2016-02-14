from app import db
from app.models.continents import Continent


class Country(db.Model):
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


