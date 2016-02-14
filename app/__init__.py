from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.Development')

db = SQLAlchemy(app)
db.init_app(app)

from app.api.continents import continents
app.register_blueprint(continents)

