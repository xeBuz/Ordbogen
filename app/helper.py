import sys
from flask import jsonify, request

if sys.version_info >= (3, 0):
    from http.client import responses as http_code
else:
    from httplib import responses as http_code


class APIOrdbogen(object):

    def __init__(self):
        self.json = {}
        self.success = False

    def _set_success(self, code):
        self.success = True if code < 400 else False
        self.json['success'] = self.success

    def _set_status(self, code):
        self.json['status'] = {
            'code': code,
            'message': http_code.get(code, None)
        }

    def _set_data(self, data):

        if data:
            if self.success:
                if isinstance(data, list):
                    data = [i.serialize for i in data]
                else:
                    if hasattr(data, 'serialize'):
                        data = data.serialize

                self.json['data'] = data
            else:
                self.json['error'] = {
                    'message': data
                }

    def _set_pagination(self, pagination):
        if pagination:
            pagination_links = {}
            count = len(pagination.items)
            link = "{}?count={}&page={}"

            pagination_links['first'] = link.format(request.base_url, count, 1)
            pagination_links['last'] = link.format(request.base_url, count, pagination.pages)

            if pagination.has_next:
                pagination_links['next'] = link.format(request.base_url, count, pagination.next_num)
            if pagination.has_prev:
                pagination_links['prev'] = link.format(request.base_url, count, pagination.prev_num)

            self.json['links'] = pagination_links

    def response(self, code=200, data=None, pagination=None):

        self._set_success(code)
        self._set_status(code)
        self._set_data(data)
        self._set_pagination(pagination)

        return jsonify(self.json), code

    @staticmethod
    def validate_fields(required_fields, provided_fields):
        if not all(x in provided_fields for x in required_fields):
            raise ValueError

    @staticmethod
    def get_form_values(fields, form_request):
        params = {}

        for field in fields:
            params[field] = form_request.get(field)

        return params

