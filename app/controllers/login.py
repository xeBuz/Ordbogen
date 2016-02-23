from functools import wraps
from app.models.tokens import Tokens
from app.models.users import Users
from flask import Blueprint, request, jsonify
from flask.views import MethodView
from .base import BaseController

login = Blueprint('login', __name__, url_prefix='/api/login')


class TokenAPI(MethodView, BaseController):

    def post(self):
        validate = ['email', 'password']
        try:
            self.validate_fields(validate, request.form)
        except ValueError:
            return self.response(400, 'Required fields: ' + ' '.join(validate))

        params = self.get_form_values(validate, request.form)
        user = Users.query.filter_by(email=params['email']).first()

        if user is None:
            return self.response(400, 'Invalid user')
        if not user.check_password(params['password']):
            return self.response(401)

        old_token = Tokens.query.filter_by(user_id=user.id).first()
        if old_token:
            old_token.delete()

        token = Tokens(user_id=user.id)
        token.save()

        json_response = {
            'access_key': token.key,
            'user': {
                'name': token.user.name,
                'e-mail': token.user.email,
            },
            'expiration': token.readeable_expiration
        }

        return self.response(200, json_response)

    # @staticmethod
    # def logout():
    #     token = Tokens.query.filter(Tokens.key == request.headers['Authorization']).first()
    #
    #     if token:
    #         token.delete()
    #
    #     return jsonify({'metadata': {
    #             'code': 200,
    #             'message': 'OK'
    #         }}, 200)


token_view = TokenAPI.as_view('token_api')
login.add_url_rule('/', view_func=token_view, methods=['POST'])
# login.add_url_rule('/logout', view_func=TokenAPI.logout(), methods=['POST'])


def login_required():
    def decorator(f):
        @wraps(f)
        def validate_token(*args, **kwargs):
            token = Tokens.query.filter_by(key=request.headers['Authorization']).first()
            error = None

            if token is None:
                error = 'Unauthorized Access'

            if token:
                if token.expired():
                    error = 'Login Expired'

            if error:
                return jsonify({'metadata': {
                    'code': 401,
                    'message': error
                }}, 401)

            return f(*args, **kwargs)
        return validate_token
    return decorator

