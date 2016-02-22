from app.helper import APIOrdbogen
from app.models.continents import Continent
from app.models.countries import Country
from flask import Blueprint, request, render_template

web_index = Blueprint('/', __name__, url_prefix='/')


@web_index.route('/', methods=['GET'])
def index():
    countries = Country.query.all()

    return render_template('index.html', countries=countries)


@web_index.route('/list', methods=['GET'])
def list_countries():
    countries = Country.query.all()

    return render_template('list.html', countries=countries)
