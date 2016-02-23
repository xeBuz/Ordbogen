from app.helper import APIOrdbogen
from app.models.continents import Continent
from flask import Blueprint, request
from flask.views import MethodView

continents = Blueprint('continents', __name__, url_prefix='/api/continents')


class ContinentAPI(MethodView, APIOrdbogen):

    def get(self, code):
        if code:
            query_continents = Continent.query.filter_by(code=code).first()

            if query_continents is None:
                return self.response(404)

        else:
            query_continents = Continent.query.all()

            if len(query_continents) == 0:
                return self.response(404)

        return self.response(200, query_continents)

    def post(self):
        try:
            self.validate_fields(Continent.required_fields(), request.form.keys())
        except ValueError:
            return self.response(400, 'Required fields: ' + ' '.join(Continent.required_fields()))

        params = self.get_form_values(Continent.get_columns(), request.form)

        validate = Continent.query.filter_by(code=params['code']).first()
        if validate:
            self.response(400, "The code already exists")

        new_continent = Continent(
            code=params['code'],
            name=params['name']
        )
        new_continent.save()

        return self.response(201)

    def delete(self, code):
        continent = Continent.query.filter_by(code=code).first()
        if continent is None:
            return self.response(404)

        continent.delete()
        return self.response(200)

    def put(self, code):
        continent = Continent.query.filter_by(code=code).first()
        if continent is None:
            return self.response(404)

        name = request.form.get('name')
        if name:
            continent.name = name

        continent.save()
        return self.response(200)

continent_view = ContinentAPI.as_view('continent_api')
continents.add_url_rule('/', defaults={'code': None}, view_func=continent_view, methods=['GET'])
continents.add_url_rule('/', view_func=continent_view, methods=['POST'])
continents.add_url_rule('/<int:code>', view_func=continent_view, methods=['GET', 'PUT', 'DELETE'])