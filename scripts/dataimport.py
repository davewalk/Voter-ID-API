""" 
Imports the Voter ID .csv file into a MongoDB database.
"""

import csv
import sys
from pymongo import Connection

DELIMITER = ','

# MongoDB Details
conn = Connection()
db = conn['voterapi']

db.states.drop()

states = db.states # The collection

class NestedDict(dict):
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print 'Only the filename, chief!'
    else:
        try:
            with open(sys.argv[1], 'r') as file:
                data = csv.reader(file, delimiter=DELIMITER)
                headers = next(data)[1:]

                #print headers
                
                for row in data:
                    state = NestedDict()

                    state['name'] = row[0]
                    state['info'][headers[0].lower()] = row[1]        
                    state['info'][headers[1].lower()] = int(row[2])
                    state['info'][headers[2].lower()] = row[3]
                    state['info'][headers[3].lower()] = int(row[4])
                    state['vote']['id'] = bool(row[5])
                    state['vote'][headers[5].lower()] = bool(row[6])
                    state['vote']['photo'] = bool(row[7])
                    state['vote'][headers[8].lower()] = row[9]

                    states = db.states
                    try:
                        states.insert(state)
                        print 'Saved %s data...' % row[0]
                    except Exception as err:
                        print str(err)

        except Exception as err:
            print str(err)
