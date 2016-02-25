from app.models.countries import Country
from app.models.events import Event
from flask import Blueprint, render_template

website = Blueprint('/', __name__, url_prefix='/')


@website.route('/', methods=['GET'])
def index():
    """
    Index Endpoint

    :return: template
    """
    countries = Country.query.all()

    return render_template('index.html', countries=countries)


@website.route('country', methods=['GET'])
def get_countries():
    """
    List Endpoint, with all the Countries

    :return: template
    """
    countries = Country.query.all()

    return render_template('list.html', countries=countries)


@website.route('country/<string:iso_code>', methods=['GET'])
def get_country(iso_code):
    """
    Country Endpoint, with country information and events

    :param iso_code:
    :return: template
    """
    iso_code = str(iso_code).upper()
    extras = {}
    country = Country.query.filter_by(iso_code=iso_code).first()

    if country is None:
        return render_template('error/404.html')
    else:
        events = Event.query.filter_by(country_id=country.id).all()

        if country.population and country.population_urban:
            extras['urban_population_percentage'] = 100 * float(country.population_urban) / float(country.population)
            extras['urban_population_color'] = get_color_statistics(extras['urban_population_percentage'])

        if country.fertility:
            extras['fertility_color'] = get_color_statistics(country.fertility)

        return render_template('country.html', country=country, events=events, extras=extras)


def get_color_statistics(item):
    """
    Get a color value (word) depending on a scale, based ir a provided value

    :param item:
    :return: color word
    """
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
