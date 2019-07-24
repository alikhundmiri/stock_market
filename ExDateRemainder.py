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
from exdatecode.get_file import file_name

def control_panel():
	# if sunday, create a file on /Users/alikhundmiri/stockmarket/corporate_act
	# name it as "2019_21", "YEAR_WEEK"
	# and then download the corporate_act file.
	# this will make sure we download new folder every sunday only. Keeps things consistent
	print("Stage 01 | File Update Sequence")
	download_location = create_file()
	morning_routine(download_location)

def morning_routine(download_location):

	# Fetch companies from the remainder text file
	complete_download_location = BASE_DIR + download_location + "/" + file_name
	# print("complete_download_location: {}".format(complete_download_location))
	
	exdate_within = 3
	companies_list = fetch_companies_remainder_list(complete_download_location, exdate_within)

	if companies_list == False:
		print("Stage 02 | Found no stocks with ExDate within {} days".format(exdate_within))
	# page_location = generate_html_page(companies_list)
	# notify_user(page_location, len(companies_list))


if __name__ == '__main__':
	control_panel()