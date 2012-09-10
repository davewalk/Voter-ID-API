"""
Scraps Wikipedia for state data.  Thanks, Wikipedia!
"""

import csv
import sys
import requests
from bs4 import BeautifulSoup

URL = 'http://en.wikipedia.org/wiki/List_of_U.S._states'

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print 'Only the filename, chief!'
    else:
        try:
            stateWriter = csv.writer(open(sys.argv[1], 'wb'))        
            stateWriter.writerow(['NAME', 'ABBR', 'POP', 'CAPITAL'])

            r = requests.get(URL)

            soup = BeautifulSoup(r.content)

            states = soup.find_all('table')[1].find_all('tr')[1:]
            for state in states:
                rows = state.find_all('td')
                name = rows[0].a.contents
                abbr = rows[2].contents
                pop = rows[6].contents
                cap = rows[7].a.contents
                stateWriter.writerow([name[0], abbr[0], pop[0].replace(',', ''),
                    cap[0]])

        except Exception as err:
            print str(err)
