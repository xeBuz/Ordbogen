from flask import jsonify


def response(code=200, data=None):
    """
    HTTP response Generator

    :param code: Numeric HTTP code
    :param data: Data
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
    json['metadata'] = {
        'code': code,
        'message': messages.get(code)
    }
    if data is not None:
        if success:
            json['data'] = data
        else:
            json['error'] = {
                'message': data
            }

    return jsonify(json), code
