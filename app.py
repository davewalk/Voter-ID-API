import os
from flask import Flask, request, Response, redirect, current_app
from pymongo import Connection
from functools import wraps
from urlparse import urlparse
import helpers

app = Flask(__name__)

MONGO_URL = os.environ['MONGOHQ_URL']

conn = Connection(MONGO_URL)
db = conn[urlparse(MONGO_URL).path[1:]]

@app.route("/states")
@helpers.jsonp
def getstates():
    filter = request.args.get('require', '')
    if (filter):
        if filter not in ('strict', 'id', 'photo') :
            message = ('%s is not a valid require value.  Use either strict, '
                'photo or id.' % filter)
            return helpers.bad_request_response(message)
        else:
            states = db.states.find({'vote.' + filter: True}, { '_id': False })
            return helpers.wrap_response(states)

    else:
        states = db.states.find({}, { '_id' : False })
        return helpers.wrap_response(states)

@app.route("/states/<statename>")
@helpers.jsonp
def getstate(statename):
    if len(statename) > 14:
        message = 'Too many characters to be a state name.'
        return helpers.bad_request_response(message)    
    elif len(statename) == 2:
        state = db.states.find({'info.abbr': statename.upper()}, { '_id': False })
        return helpers.wrap_response(state)
    else:
        state = db.states.find({'name': statename.title()}, { '_id': False })
        return helpers.wrap_response(state)

if __name__ == "__main__":
    app.run(debug=False)
