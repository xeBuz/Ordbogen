from flask import jsonify


def response(code=200, data=None, pagination=None, url=None):
    """
    HTTP response Generator

    :param code: Numeric HTTP code
    :param data: Data
    :param pagination: Pagination object
    :param url: Base URL to build the pagination
    :return: HTTP Response
    """
    json = {}
    messages = {
        200: 'Success',
        201: 'Created',
        202: 'Accepted',
        204: 'No Content',
        400: 'Bad Request',
        401: 'Unauthorized',
        403: 'Forbidden',
        404: 'Not Found',
        406: 'Not Acceptable',
        410: 'Gone',
        422: 'Unprocesable entity',
        500: 'Internal Error',
        501: 'Not implemented',
        503: 'Service Unavailable',
        504: 'Gateway Timeout',
        505: 'HTTP Version Not Supported'
    }

    success = True if code < 400 else False

    json['success'] = success
    json['status'] = {
        'code': code,
        'message': messages.get(code)
    }
    if data is not None:
        if success:
            if isinstance(data, list):
                data = [i.serialize for i in data]
            else:
                if hasattr(data, 'serialize'):
                    data = data.serialize

            json['data'] = data
        else:
            json['error'] = {
                'message': data
            }

    if pagination is not None:
        pagination_links = {}
        count = len(pagination.items)
        link = "{}?count={}&page={}"

        pagination_links['first'] = link.format(url, count, 1)
        pagination_links['last'] = link.format(url, count, pagination.pages)

        if pagination.has_next:
            pagination_links['next'] = link.format(url, count, pagination.next_num)
        if pagination.has_prev:
            pagination_links['prev'] = link.format(url, count, pagination.prev_num)

        json['links'] = pagination_links

    return jsonify(json), code



