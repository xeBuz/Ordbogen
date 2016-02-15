from app.helper import response
from flask import Blueprint, request
from app.models.countries import Country

countries = Blueprint('countries', __name__, url_prefix='/api/countries')


@countries.route('/', methods=['GET'])
@countries.route('/<string:iso_code>', methods=['GET'])
def get(iso_code=None):

    if iso_code:
        pagination = None
        iso_code = str(iso_code).upper()
        query_countries = Country.query.filter_by(iso_code=iso_code).first()

        if query_countries is None:
            return response(404)

    else:
        page = int(request.args.get('page', '1'))
        count = int(request.args.get('count', '5'))
        sort = request.args.get('sort', 'iso_code')

        pagination = Country.query.order_by(sort).paginate(page, count, False)
        query_countries = pagination.items

        if len(query_countries) == 0:
            return response(404)

    return response(200, query_countries, pagination, request.base_url)


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
    country = Country.query.filter_by(iso_code=iso_code).first()
    if country is None:
        return response(404)

    country.delete()
    return response(200)

