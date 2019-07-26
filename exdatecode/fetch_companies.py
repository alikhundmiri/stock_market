import csv
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os
# from exdatecode.file_and_folder_processing import get_latest_file
# from exdatecode.file_and_folder_processing import BASE_DIR
# from exdatecode.get_file import file_name

from exdatecode.notify import notify

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
		return_list.append(row)
		# print("Buy Stock of '{}' \nin {} days. \nOffer: {}.\n-------------\n".format(row[2], str(delta.days), row[4]))
		return True
	else:
		return False
	

def get_list(week):
	# print("this script will fetch companies with exdate in next few weeks, namely:")
	print("date: {}".format(week[3]))
	print("date format: {}".format(type(week[3])))

	companies_with_exdates(week)

def companies_with_exdates(week):
	# from file in download folder, get companies with ex date, and add the row to the return_list[]
	return_list.append(week)

def fetch_companies_remainder_list(file_location, exdate_within):
	print("Stage 02 | Reading file")
	company_counter = 0
	with open(file_location, 'r') as csvFile:
		reader = csv.reader(csvFile)
		# This CSV file has a header. So we need to skop the first row. This line below does just that
		next(reader)
		for row in reader:

			interested_stock = check_date(row, days_within=exdate_within)
			if interested_stock:
				company_counter += 1

	print("Stage 02 | Found {} companies with exdate with {} days".format(company_counter, exdate_within))

	# print("Stage 02 | Printing List:\n")

	# for row in return_list:
	# 	print("Buy Stock of '{}' \nin {} days. \nOffer: {}.\n-------------\n".format(row[2], row[3], row[4]))
		

	csvFile.close()
	if not return_list:
		return False
	else:
		return return_list

# if __name__ == '__main__':
	# get_list([1, 3, 5])
	# file_location = BASE_DIR + get_latest_file() + file_name
	# exdate_within = 7
	# fetch_companies_remainder_list(file_location, exdate_within)
	