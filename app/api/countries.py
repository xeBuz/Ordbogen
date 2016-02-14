from app.helper import response
from flask import Blueprint, request
from app.models.countries import Country

countries = Blueprint('countries', __name__, url_prefix='/api/countries')


@countries.route('/', methods=['GET'])
@countries.route('/<string:iso_code>', methods=['GET'])
def get(iso_code=None):

    if iso_code:
        query_countries = Country.query.filter_by(iso_code=iso_code).all()
    else:
        query_countries = Country.query.all()

    if len(query_countries) == 0:
        return response(404)

    json_list = [i.serialize for i in query_countries]
    return response(200, json_list)


@countries.route('/', methods=['POST'])
def post():
    code = request.form.get('code')
    return "POST"
    # errors = []
    # code = request.form.get('code')
    # name = request.form.get('name')
    #
    # if name is None:
    #     errors.append("Invalid name value")
    # if code is None:
    #     errors.append("Invalid code value")
    # else:
    #     validate = Continent.query.filter_by(code=code).first()
    #     if validate:
    #         errors.append("The code already exists")
    #
    # if errors:
    #     return response(400, errors)
    #
    # new_continent = Continent(code=code, name=name)
    # new_continent.save()
    #
    # return response(201)


@countries.route('/<string:iso_code>', methods=['PUT'])
def put(iso_code):
    return "PUT"
    # continent = Continent.query.filter_by(code=code).first()
    # if continent is None:
    #     return response(404)
    #
    # name = request.form.get('name')
    # if name:
    #     continent.name = name
    #
    # return response(200)


@countries.route('/<string:isocode>', methods=['DELETE'])
def delete(iso_code):
    return "DELETE"
    # continent = Country.query.filter_by(code=code).first()
    # if continent is None:
    #     return response(404)
    #
    # continent.delete()
    # return response(200)

