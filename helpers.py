import json
from bson import json_util
from flask import Flask, request, Response, redirect, current_app
from functools import wraps

def jsonp(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            content = str(callback) + '(' + str(f(*args, **kwargs).data) + ')'
            return current_app.response_class(content, 
                    mimetype='application/javascript')
        else: 
            return f(*args, **kwargs)
    return decorated_function

def wrap_response(states):
    data = str(json.dumps({'results': list(states)},
        default = json_util.default,
        indent = 4))
    response = Response(data, status=200, mimetype='application/json')
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

def bad_request_response(message):
    data = str(json.dumps({'error': 
                            {'id': '400 Bad Request',
                             'message': '400 Bad Request: ' + message}},
        default = json_util.default,
        indent = 4))
    response = Response(data, status=400, mimetype='application/json')
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
