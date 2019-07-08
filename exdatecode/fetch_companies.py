import json
import requests
from bs4 import BeautifulSoup

return_list = []

def get_list(week_list):
	print("this script will fetch companies with exdate in next few weeks, namely:")
	for week in week_list:
		companies_with_exdates(week)

def companies_with_exdates(week):
	# from file in download folder, get companies with ex date, and add the row to the return_list[]
	print("week {}".format(week))

if __name__ == '__main__':
	get_list([1, 3, 5])