from app.helper import APIOrdbogen
from flask import Blueprint, request
from flask.views import MethodView
from app.models.countries import Country
from app.models.continents import Continent

countries = Blueprint('countries', __name__, url_prefix='/api/countries')


class CountryAPI(MethodView, APIOrdbogen):

    def get(self, iso_code):
        allowed_sort = ['iso_code', 'short_name', 'country_code']
        print iso_code
        if iso_code:
            pagination = None
            iso_code = str(iso_code).upper()
            query_countries = Country.query.filter_by(iso_code=iso_code).first()

            if query_countries is None:
                return self.response(404)

        else:
            page = int(request.args.get('page', '1'))
            count = int(request.args.get('count', '5'))
            sort = request.args.get('sort', 'iso_code')
            name = request.args.get('name')

            if sort not in allowed_sort:
                return self.response(400, 'Invalid sort field')

            if name:
                if len(name) < 2:
                    return self.response(400, 'Minimum length allowed for name: 2')

                pagination = Country.query.filter(Country.short_name.like(name + "%"))\
                    .order_by(sort).paginate(page, count, False)
            else:
                pagination = Country.query.order_by(sort).paginate(page, count, False)

            query_countries = pagination.items

            if len(query_countries) == 0:
                return self.response(404)

        return self.response(200, query_countries, pagination)

    def post(self):
        errors = []

        iso_code = request.form.get('iso_code')
        iso_code_long = request.form.get('iso_code_long')
        short_name = request.form.get('short_name')
        formal_name = request.form.get('formal_name')
        demonym = request.form.get('demonym')
        country_code = request.form.get('country_code')
        continental_code = request.form.get('continental_code')
        coordinates = request.form.get('coordinates')
        elevation = request.form.get('elevation')
        elevation_low = request.form.get('elevation_low')
        area = request.form.get('area')
        land = request.form.get('land')
        fertility = request.form.get('fertility')
        population = request.form.get('population')
        population_urban = request.form.get('population_urban')
        itu = request.form.get('itu')
        web = request.form.get('web')
        gis = request.form.get('gis')
        statistics = request.form.get('statistics')
        flag = request.form.get('flag'),
        government = request.form.get('government')
        boundary_box = request.form.get('boundary_box')
        currency = request.form.get('currency')

        if iso_code is None:
            errors.append("Invalid iso_code value")
        else:
            validate = Country.query.filter_by(iso_code=iso_code).first()
            if validate:
                errors.append("The iso_code already exists")
        if continental_code:
            validate = Continent.query.filter_by(code=continental_code).first()
            if validate is None:
                errors.append("The continental_code doesn't exists")

        if errors:
            return self.response(400, errors)

        new_continent = Country(
            iso_code=iso_code,
            iso_code_long=iso_code_long,
            short_name=short_name,
            formal_name=formal_name,
            demonym=demonym,
            country_code=country_code,
            continental_code=continental_code,
            coordinates=coordinates,
            elevation=elevation,
            elevation_low=elevation_low,
            area=area,
            land=land,
            fertility=fertility,
            population=population,
            population_urban=population_urban,
            itu=itu,
            web=web,
            gis=gis,
            statistics=statistics,
            flag=flag,
            government=government,
            boundary_box=boundary_box,
            currency=currency,
        )
        new_continent.save()

        return self.response(201)

    def delete(self, iso_code):
        country = Country.query.filter_by(iso_code=iso_code).first()
        if country is None:
            return self.response(404)

        country.delete()
        return self.response(200)

    def put(self, iso_code):
        errors = []
        iso_code = str(iso_code).upper()
        country = Country.query.filter_by(iso_code=iso_code).first()

        if country is None:
            return self.response(404)

        iso_code_long = request.form.get('iso_code_long')
        short_name = request.form.get('short_name')
        formal_name = request.form.get('formal_name')
        demonym = request.form.get('demonym')
        country_code = request.form.get('country_code')
        continental_code = request.form.get('continental_code')
        coordinates = request.form.get('coordinates')
        elevation = request.form.get('elevation')
        elevation_low = request.form.get('elevation_low')
        area = request.form.get('area')
        land = request.form.get('land')
        fertility = request.form.get('fertility')
        population = request.form.get('population')
        population_urban = request.form.get('population_urban')
        itu = request.form.get('itu')
        web = request.form.get('web')
        gis = request.form.get('gis')
        statistics = request.form.get('statistics')
        flag = request.form.get('flag'),
        government = request.form.get('government')
        boundary_box = request.form.get('boundary_box')
        currency = request.form.get('currency')

        if continental_code:
            validate = Continent.query.filter_by(code=continental_code).first()
            if validate is None:
                errors.append("The continental_code doesn't exists")
        if errors:
            return self.response(400, errors)

        if iso_code_long:
            country.iso_code_long = iso_code_long
        if short_name:
            country.short_name = short_name
        if formal_name:
            country.formal_name = formal_name
        if demonym:
            country.demonym = demonym
        if country_code:
            country.country_code = country_code
        if continental_code:
            country.continental_code = continental_code
        if coordinates:
            country.coordinates = coordinates
        if elevation:
            country.elevation = elevation
        if elevation_low:
            country.elevation_low = elevation_low
        if area:
            country.area = area
        if land:
            country.land = land
        if fertility:
            country.fertility = fertility
        if population:
            country.population = population
        if population_urban:
            country.population_urban = population_urban
        if itu:
            country.itu = itu
        if web:
            country.web = web
        if gis:
            country.gis = gis
        if statistics:
            country.statistics = statistics
        if flag:
            country.flag = flag
        if government:
            country.government = government
        if boundary_box:
            country.boundary_box = boundary_box
        if currency:
            country.currency = currency

        country.save()
        return self.response(200)

country_view = CountryAPI.as_view('country_api')
countries.add_url_rule('/', defaults={'iso_code': None}, view_func=country_view, methods=['GET'])
countries.add_url_rule('/', view_func=country_view, methods=['POST'])
countries.add_url_rule('/<string:iso_code>', view_func=country_view, methods=['GET', 'PUT', 'DELETE'])


