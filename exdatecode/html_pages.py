import glob


import os
import datetime
from exdatecode.notify import notify
from exdatecode.file_and_folder_processing import BASE_DIR, get_latest_file


def generate_html_page(companies_list):
	week_dir = get_latest_file()
	html_location  = BASE_DIR + "" + week_dir
	print(html_location)
	for company in companies_list:
		print(company)
	return True


def send_emails(html_content):
	pass