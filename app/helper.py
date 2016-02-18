from flask import jsonify, request
from httplib import responses as http_code


class APIOrdbogen(object):

    json = {}

    def _is_success(self, code):
        return True if code < 400 else False

    def _set_success(self, sucess=False):
        self.json['success'] = sucess

    def _set_status(self, code):
        self.json['status'] = {
            'code': code,
            'message': http_code.get(code, None)
        }

    def _set_data(self, data, success):

        if data:
            if success:
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
        success =  self._is_success(code)

        self._set_success(success)
        self._set_status(code)
        self._set_data(data, success)
        self._set_pagination(pagination)

        return jsonify(self.json), code
