import glob


import os
import datetime
from exdatecode.notify import notify
from exdatecode.get_file import download_file, file_name

BASE_DIR = "/Users/alikhundmiri/stockmarket/corporate_act/"

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
		folder_name = "{}_{}".format(this_year, this_week)

		# generate the new src file
		download_location = BASE_DIR + folder_name
		# and finally create the folder, taking the measures, dont create folder if it already exists
		if os.path.exists(download_location):
			print("Stage 01 | TEST | folder '{}' exists".format(folder_name))
			file_download_location = download_location + "/" + file_name
			if os.path.exists(file_download_location):
				print("Stage 01 | TEST | file '{}' exists. No need to download".format(file_name))
				print("Stage 01 | File Update Sequence | File Already Downloaded")
				return folder_name
			else:
				print("Stage 01 | TEST | Folder '{}' exists, but file '{}' doesnt exist. Creating file".format(folder_name, file_name))
				os.makedirs(download_location)
		else:		
			os.makedirs(download_location)

		print("Stage 01 | File Update Sequence | Downloading New File")
		# download the new corporate act file.
		download_file(download_location)

		# and then return the new file name
		return folder_name
	else:
		print("Stage 01 | File Update Sequence | Fetching Old File")

		# if today is not sunday, simply get the old folder name. If we created it the file name can be Guessed.
		return get_latest_file()

def today_is_sunday():
	if datetime.datetime.today().weekday() == 6:
		return True
	else:
		return False

def get_latest_file():

	# code from StackOverflow : https://stackoverflow.com/a/39327156/6518499
	# this snippet will get the list of files, and then fetch the last one

	list_of_files = glob.glob(BASE_DIR+"*") # * means all if need specific format then *.csv

	latest_file = max(list_of_files, key=os.path.getctime)
	
	latest_file = latest_file.replace(BASE_DIR, '')
	return latest_file


	