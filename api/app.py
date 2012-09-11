import os
import sys
import json
from flask import Flask
from flask import request
from pymongo import Connection
from bson import json_util
from urlparse import urlparse

app = Flask(__name__)

MONGO_URL = os.environ['MONGOHQ_URL']

conn = Connection(MONGO_URL)
db = conn[urlparse(MONGO_URL).path[1:]]

@app.route("/states")
def getstates():
    filter = request.args.get('required', '')
    if (filter):
        states = db.states.find({'vote.' + filter: True}, { '_id': False })
        return str(json.dumps({'results': list(states)},
            default = json_util.default,
            indent=4))
    else:
        states = db.states.find()
        return str(json.dumps({'results' : list(states)}, 
            default = json_util.default,
            indent=4))

@app.route("/states/<statename>")
def getstate(statename):
    try:
        if len(statename) == 2:
            state = db.states.find({'info.abbr': statename})
            return str(json.dumps({'results': list(state)},
                default = json_util.default,
                indent=4))
        else:
            state = db.states.find({'name': statename})
            return str(json.dumps({'results': list(state)},
                default = json_util.default,
                indent=4))
    except Exception as err:
        return str(err)

if __name__ == "__main__":
    app.run(debug=False)
