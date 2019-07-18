'''
how it works

1. get a list of all companies who give dividend.
2. get the ex date (the date before which you must buy stock to get dividend)
3. get the stock amount
4. get teh dividend amount
5. add it to remainder list

go though all remainder list
1. if date of ex-date is upcoming, add to notify list.
2. on computer startup in morning, run the notify list,
3. send the notification "You have {} companies who exdate is this week"
4. when click on the notification, launch a webpage, with list of all stocks and links
'''

from exdatecode.fetch_companies import companies_with_exdates
from exdatecode.fetch_companies import fetch_companies_remainder_list
from exdatecode.file_and_folder_processing import generate_html_page
from exdatecode.file_and_folder_processing import notify_user
from exdatecode.file_and_folder_processing import create_file
from exdatecode.file_and_folder_processing import BASE_DIR

def control_panel():

	# if sunday, create a file on /Users/alikhundmiri/stockmarket/corporate_act
	# name it as "2019_21", "YEAR_WEEK"
	# and then download the corporate_act file.
	# this will make sure we download new folder every sunday only. Keeps things consistent
	print("Stage 01 | File Update Sequence")
	download_location = create_file()
	complete_download_location = BASE_DIR + download_location

	
	# update the stock list queue
	# exdate_within_weeks = [1, 3]
	# companies_with_exdates(exdate_within_weeks)

def morning_routine():
	# Fetch companies from the remainder text file
	companies_list = fetch_companies_remainder_list()
	page_location = generate_html_page(companies_list)
	notify_user(page_location, len(companies_list))


if __name__ == '__main__':
	control_panel()