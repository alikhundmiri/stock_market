import os
import json
import glob
import datetime
from exdatecode.notify import notify
from exdatecode.file_and_folder_processing import BASE_DIR, get_latest_file


def generate_html_page(companies_list):
	week_dir = get_latest_file()
	html_location  = BASE_DIR + "" + week_dir

	json_data = json.dumps(companies_list)
	today_date = datetime.datetime.today()

	print(today_date)
	# for company in companies_list:
	# 	print(company[3])
	return True


def send_emails(html_content):
	pass