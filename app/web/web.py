from app.models.countries import Country
from flask import Blueprint, render_template

website = Blueprint('/', __name__, url_prefix='/')


@website.route('/', methods=['GET'])
def index():
    countries = Country.query.all()

    return render_template('index.html', countries=countries)


@website.route('country', methods=['GET'])
def get_countries():
    countries = Country.query.all()

    return render_template('list.html', countries=countries)


@website.route('country/<string:iso_code>', methods=['GET'])
def get_country(iso_code):
    iso_code = str(iso_code).upper()
    extras = {}
    country = Country.query.filter_by(iso_code=iso_code).first()

    if country is None:
        return render_template('error/404.html')
    else:

        if country.population and country.population_urban:
            extras['urban_population_percentage'] = 100 * float(country.population_urban) / float(country.population)
            extras['urban_population_color'] = get_color_stadistics(extras['urban_population_percentage'])

        if country.fertility:
            extras['fertility_color'] = get_color_stadistics(country.fertility)

        return render_template('country.html', country=country, extras=extras)


def get_color_stadistics(item):
    if item > 90:
        color = 'green'
    elif item > 70:
        color = 'teal'
    elif item > 50:
        color = 'orange'
    elif item > 30:
        color = 'yellow'
    else:
        color = 'red'

    return color
