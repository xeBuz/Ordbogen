from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(
    __name__,
    template_folder='../templates',
    static_folder='../statics'
)

app.config.from_object('config.Development')

db = SQLAlchemy(app)
db.init_app(app)

from app.api.continents import continents
from app.api.countries import countries
from app.api.events import events

app.register_blueprint(continents)
app.register_blueprint(countries)
app.register_blueprint(events)

from app.web.web import website
app.register_blueprint(website)
