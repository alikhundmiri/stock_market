import csv
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime

return_list = []

def get_list(week):
	# print("this script will fetch companies with exdate in next few weeks, namely:")
	print("date: {}".format(week[3]))
	print("date format: {}".format(type(week[3])))

	companies_with_exdates(week)

def companies_with_exdates(week):
	# from file in download folder, get companies with ex date, and add the row to the return_list[]
	return_list.append(week)


def fetch_companies_remainder_list(file_location):
	print("Stage 2 | reading file")
	with open(file_location, 'r') as csvFile:
		reader = csv.reader(csvFile)
		next(reader)
		for row in reader:
			datetime_object = datetime.strptime(row[3], '%d %b %Y')
						
			# get_list(row)
	
	csvFile.close()

	# for item in return_list:
		# print(item)

if __name__ == '__main__':
	get_list([1, 3, 5])