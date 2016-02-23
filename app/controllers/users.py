from .base import BaseController
from flask import Blueprint, request
from app.models.users import Users
from flask.views import MethodView

users = Blueprint('users', __name__, url_prefix='/api/users')


class UsersAPI(MethodView, BaseController):

    def get(self, user_id):
        if user_id:
            pagination = None
            query_users = Users.query.filter_by(id=user_id).first()
            if query_users is None:
                return self.response(404)

        else:
            page = int(request.args.get('page', '1'))
            count = int(request.args.get('count', '5'))

            pagination = Users.query.paginate(page, count, False)
            query_users = pagination.items

            if len(query_users) == 0:
                return self.response(404)

        return self.response(200, query_users, pagination)

    def post(self):
        try:
            self.validate_fields(Users.required_fields(), request.form)
        except ValueError:
            return self.response(400, 'Required fields: ' + ' '.join(Users.required_fields()))

        params = self.get_form_values(Users.get_columns(), request.form)

        new_user = Users(
            name=params['name'],
            email=params['email'],
            password=params['password']
        )
        new_user.save()

        return self.response(201)

    def delete(self, user_id):
        user = Users.query.filter_by(id=user_id).first()
        if user is None:
            return self.response(404)

        user.delete()
        return self.response(200)


user_view = UsersAPI.as_view('user_api')
users.add_url_rule('/', defaults={'user_id': None}, view_func=user_view, methods=['GET'])
users.add_url_rule('/', view_func=user_view, methods=['POST'])
users.add_url_rule('/<int:user_id>', view_func=user_view, methods=['GET', 'DELETE'])
