
__author__ = 'apeckys'

import requests
import csv
from optparse import OptionParser
import sys
 

def __main():
	parser = OptionParser("%prog [options]")
	parser.add_option("-f", "--file", dest="filename", default=False, action="store", help="specify output file")
	(options, args) = parser.parse_args(sys.argv or sys.argv[1:])
	
	geekData = getData()
	print 'Found {} performers'.format(len(geekData))
	writeCsv(options.filename, geekData)

def getData():
	url = 'https://api.seatgeek.com/2/events?per_page=2000&venue.city=chicago&type=concert'
	r = requests.get(url)
	
	results = []
	data = r.json()
	for entry in data['events']:
		for perfomer in entry['performers']:
			results.append({
				"datetime_local": entry['datetime_local'],
				"performers_name": perfomer['name'],
				"venue_name": entry['venue']['name']
			})

	return results


def writeCsv(fileName, data):
	file_handle = open(fileName, 'w')
	csvwriter = csv.writer(file_handle)
	count = 0

	for entry in data:
		if count == 0:
			header = entry.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(entry.values())
	file_handle.close()

# This is the conventional entry point for the start of the main script
if __name__ == '__main__':
	__main()
