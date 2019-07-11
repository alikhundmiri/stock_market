import os
import datetime
from exdatecode.notify import notify
from exdatecode.get_file import download_file

BASE_DIR = "/Users/alikhundmiri/stockmarket/corporate_act/"

def generate_html_page(companies_list):
	for company in companies_list:
		print(company)

def notify_user(page_location, number_of_companies):
	title = 'Downloading...'
	text = 'creating a file of {} companies'.format(number_of_companies)
	subtitle = None
	notify(title, text, subtitle)

def create_file():
	# This function, creates a folder if it doesnt exist
	# get todays date,
	now = datetime.datetime.now()
	# get the year
	this_year = now.year
	# get the week number
	this_week = now.isocalendar()[1]

	# check if today is sunday
	if today_is_sunday():
		# if it is sunday, create a new folder
		file_name = "{}_{}".format(this_year, this_week)

		# generate the new src file
		src = BASE_DIR + file_name

		# and finally create the folder, taking the measures, dont create folder if it already exists
		if not os.path.exists(src):
			os.makedirs(src)

		# download the new corporate act file.
		download_file(download_location)

		# and then return the new file name
		return file_name
	else:
		# if today is not sunday, simply get the old folder name. If we created it the file name can be Guessed.
		return get_latest_file(this_year, this_week)

def today_is_sunday():
	if datetime.datetime.today().weekday() == 6:
		return True
	else:
		return False

def get_latest_file(this_year, this_week):

	# need to work on this logic.
	if this_week == 52:
		this_week = 1
		this_year =+ 1

	file_name = "{}_{}".format(this_year, this_week)
	return file_name


	