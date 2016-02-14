from app.helper import response
from app.models.continents import Continent
from flask import Blueprint, request

continents = Blueprint('continents', __name__, url_prefix='/api/continents')


@continents.route('/', methods=['GET'])
@continents.route('/<int:code>', methods=['GET'])
def get(code=None):

    if code:
        query_continents = Continent.query.filter_by(code=code).all()
    else:
        query_continents = Continent.query.all()

    if len(query_continents) == 0:
        return response(404)

    json_list = [i.serialize for i in query_continents]
    return response(200, json_list)


@continents.route('/', methods=['POST'])
def post():
    errors = []
    code = request.form.get('code')
    name = request.form.get('name')

    if name is None:
        errors.append("Invalid name value")
    if code is None:
        errors.append("Invalid code value")
    else:
        validate = Continent.query.filter_by(code=code).first()
        if validate:
            errors.append("The code already exists")

    if errors:
        return response(400, errors)

    new_continent = Continent(code, name)
    new_continent.save()

    return response(201)


@continents.route('/<int:code>', methods=['PUT'])
def put(code):
    continent = Continent.query.filter_by(code=code).first()
    if continent is None:
        return response(404)

    name = request.form.get('name')
    if name:
        continent.name = name

    return response(200)


@continents.route('/<int:code>', methods=['DELETE'])
def put(code):
    continent = Continent.query.filter_by(code=code).first()
    if continent is None:
        return response(404)

    continent.delete()

    return response(200)

