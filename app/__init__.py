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

from app.controllers.continents import continents
from app.controllers.countries import countries
from app.controllers.events import events
from app.controllers.users import users
from app.controllers.login import login

app.register_blueprint(continents)
app.register_blueprint(countries)
app.register_blueprint(events)
app.register_blueprint(users)
app.register_blueprint(login)

from app.web.web import website
app.register_blueprint(website)
