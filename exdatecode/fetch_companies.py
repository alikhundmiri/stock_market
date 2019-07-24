import csv
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime

return_list = []

# This is today's date, in datetime format
today_date = datetime.today()


def check_date(row, days_within):
	# this is the ex date of selected stock, in datetime format
	ex_date = datetime.strptime(row[3], '%d %b %Y')

	# the difference between two dates
	delta = ex_date - today_date
	
	# if the stock's exdate is with in this range, do something.
	if 0 < delta.days < days_within:
		print("Buy Stock of '{}' \nin {} days. \nOffer: {}.\n-------------\n".format(row[2], str(delta.days), row[4]))
	pass

def get_list(week):
	# print("this script will fetch companies with exdate in next few weeks, namely:")
	print("date: {}".format(week[3]))
	print("date format: {}".format(type(week[3])))

	companies_with_exdates(week)

def companies_with_exdates(week):
	# from file in download folder, get companies with ex date, and add the row to the return_list[]
	return_list.append(week)


def fetch_companies_remainder_list(file_location):
	print("Stage 02 | reading file")
	with open(file_location, 'r') as csvFile:
		reader = csv.reader(csvFile)
		
		# This CSV file has a header. So we need to skop the first row. This line below does just that
		next(reader)
		for row in reader:
			# datetime_object = datetime.strptime(row[3], '%d %b %Y')
			check_date(row, days_within=21)
			# get_list(row)
	
	csvFile.close()

	# for item in return_list:
		# print(item)

if __name__ == '__main__':
	get_list([1, 3, 5])