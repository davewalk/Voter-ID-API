import json
from flask import Flask
from flask import request
from pymongo import Connection
from bson import json_util
from copy import deepcopy

app = Flask(__name__)

# MongoDB Details
conn = Connection()
db = conn['voterapi']

states = db.states

@app.route("/states")
def getstates():
    # Get and return states documents from DB.
    filter = request.args.get('required', '')
    if (filter):
        #states = db.states.find({'.'.join(['vote', filter]) : true }, 
        #        {' _id': False })
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
    # Get the passed state name and return the state's document from DB.
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
    app.run(debug=True)

    #states = db.states.find({ "name" : 'Pennsylvania' })
    #print str(json.dumps({'states': list(states)},
    #    default = json_util.default))
