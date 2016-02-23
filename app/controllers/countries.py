from .base import BaseController
from flask import Blueprint, request
from flask.views import MethodView
from app.models.countries import Country
from app.models.continents import Continent
from app.controllers.login import login_required

countries = Blueprint('countries', __name__, url_prefix='/api/countries')


class CountryAPI(MethodView, BaseController):

    def get(self, iso_code):
        allowed_sort = ['iso_code', 'short_name', 'country_code']
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

    @login_required()
    def post(self):
        errors = []
        try:
            self.validate_fields(Country.required_fields(), request.form)
        except ValueError:
            return self.response(400, 'Required fields: ' + ' '.join(Country.required_fields()))

        params = self.get_form_values(Country.get_columns(), request.form)

        validate = Country.query.filter_by(iso_code=params['iso_code']).first()
        if validate:
            errors.append("The iso_code already exists")

        if params['continental_code']:
            validate = Continent.query.filter_by(code=params['continental_code']).first()
            if validate is None:
                errors.append("The continental_code doesn't exists")

        if errors:
            return self.response(400, errors)

        new_country = Country(
            iso_code=params['iso_code'],
            iso_code_long=params['iso_code_long'],
            short_name=params['short_name'],
            formal_name=params['formal_name'],
            demonym=params['demonym'],
            country_code=params['country_code'],
            continental_code=params['continental_code'],
            coordinates=params['coordinates'],
            elevation=params['elevation'],
            elevation_low=params['elevation_low'],
            area=params['area'],
            land=params['land'],
            fertility=params['fertility'],
            death=params['death'],
            birth=params['birth'],
            population=params['population'],
            population_urban=params['population_urban'],
            itu=params['itu'],
            web=params['web'],
            gis=params['gis'],
            statistics=params['statistics'],
            flag=params['flag'],
            government=params['government'],
            boundary_box=params['boundary_box'],
            currency=params['currency'],
        )
        new_country.save()

        return self.response(201)

    @login_required()
    def delete(self, iso_code):
        country = Country.query.filter_by(iso_code=iso_code).first()
        if country is None:
            return self.response(404)

        country.delete()
        return self.response(200)

    @login_required()
    def put(self, iso_code):
        errors = []
        iso_code = str(iso_code).upper()
        country = Country.query.filter_by(iso_code=iso_code).first()

        if country is None:
            return self.response(404)

        params = self.get_form_values(Country.get_columns(), request.form)

        if params['continental_code']:
            validate = Continent.query.filter_by(code=params['continental_code']).first()
            if validate is None:
                errors.append("The continental_code doesn't exists")
        if errors:
            return self.response(400, errors)

        if params['iso_code_long']:
            country.iso_code_long = params['iso_code_long']
        if params['short_name']:
            country.short_name = params['short_name']
        if params['formal_name']:
            country.formal_name = params['formal_name']
        if params['demonym']:
            country.demonym = params['demonym']
        if params['country_code']:
            country.country_code = params['country_code']
        if params['continental_code']:
            country.continental_code = params['continental_code']
        if params['coordinates']:
            country.coordinates = params['coordinates']
        if params['elevation']:
            country.elevation = params['elevation']
        if params['elevation_low']:
            country.elevation_low = params['elevation_low']
        if params['area']:
            country.area = params['area']
        if params['land']:
            country.land = params['land']
        if params['fertility']:
            country.fertility = params['fertility']
        if params['population']:
            country.population = params['population']
        if params['population_urban']:
            country.population_urban = params['population_urban']
        if params['itu']:
            country.itu = params['itu']
        if params['web']:
            country.web = params['web']
        if params['gis']:
            country.gis = params['gis']
        if params['statistics']:
            country.statistics = params['statistics']
        if params['flag']:
            country.flag = params['flag']
        if params['government']:
            country.government = params['government']
        if params['boundary_box']:
            country.boundary_box = params['boundary_box']
        if params['currency']:
            country.currency = params['currency']

        country.save()
        return self.response(200)

country_view = CountryAPI.as_view('country_api')
countries.add_url_rule('/', defaults={'iso_code': None}, view_func=country_view, methods=['GET'])
countries.add_url_rule('/', view_func=country_view, methods=['POST'])
countries.add_url_rule('/<string:iso_code>', view_func=country_view, methods=['GET', 'PUT', 'DELETE'])


