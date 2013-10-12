#!/usr/bin/env python

import csv
import json

inputcsv = [ 'svc' ]

for csvfile in inputcsv:
	f = open(csvfile + '.csv' , 'r')

	reader = csv.reader(f, delimiter=',', quotechar='"')
	keys = next(reader) #skip the headers  
	out = [{key: val for key, val in zip(keys, prop)} for prop in reader]
	f.close()

	f = open(csvfile + '.json', 'w')
	f.write( json.dumps(out) )
	f.close


