#!/usr/bin/env python

import csv
import json

inputcsv = [ 'svc' ]

def main():
	for csvfile in inputcsv:
		infile = csvfile + '.csv'
		outfile = csvfile + '.json'
		csvToJson(infile, outfile)
		"""
		f = open(csvfile + '.csv' , 'r')

		reader = csv.reader(f, delimiter=',', quotechar='"')
		keys = next(reader) #skip the headers  
		out = [{key: val for key, val in zip(keys, prop)} for prop in reader]
		f.close()

		f = open(csvfile + '.json', 'w')
		f.write( json.dumps(out) )
		f.close
		"""

def csvToJson( inFile, outFile ):
    out = None;

    with open( inFile, 'r') as csvFile:
        #Note this reads the first line as the keys we can add specific keys with:
        #csv.DictReader( csvFile, fieldnames=<LIST HERE>, restkey=None, restval=None, )
        csvDict = csv.DictReader( csvFile, restkey=None, restval=None, )
        out = [obj for obj in csvDict]

    if out:
        with open( outFile, 'w' ) as jsonFile:
            jsonFile.write( json.dumps( out ) );
    else:
       print "Error creating csv dict!"

if __name__=="__main__":
	main()
