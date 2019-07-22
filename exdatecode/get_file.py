from selenium import webdriver
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time
import os

from exdatecode.notify import notify

url = 'https://www.bseindia.com/corporates/corporate_act.aspx'

file_name = 'Corporate_Actions.csv'

old_location = '/Users/alikhundmiri/Downloads/' + file_name

def launch_chrome():
	global driver
	print("Stage 01 | Launching Chrome...")
	notify("Launching Chrome...", "Attempting to download Corporate Act", None)
	driver = webdriver.Chrome('/Library/SeleniumWebDrivers/WebDrivers/chromedriver')
	time.sleep(1)


def open_website(page_link):
	#open page
	driver.get(page_link)

	assert "BSEINDIA" in driver.title
	print("Stage 01 | Website is open!")

	download_button = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_lnkDownload1"]')
	print("Stage 01 | Attempting to Downloading file...")

	download_button.click()
	print("Stage 01 | download started...")


	# not using this code
def check_download_file():
	print("looking at location: {}".format(old_location))
	while not os.path.exists(old_location):
		print('Checking for download...')
		time.sleep(1)

	if os.path.isfile(old_location):
		print("Stage 01 | downloaded file name: {}".format(file_name))	
	else:
		raise ValueError("%s isn't a file!" % file_path)

	print("Stage 01 | file Download Complete")



def move_download_file(download_location):
	new_location = download_location + "/" + file_name
	try:
		os.rename(old_location, new_location)
		print("Stage 01 | file Transfer Complete!")
		return True

	except os.error:
		print("ERROR | Can't move file from download to archive")
		return False

def download_file(download_location):
	launch_chrome()
	open_website(url)
	# waits for all the files to be completed and returns the paths
	check_download_file()

	if move_download_file(download_location):
		driver.close()
		return True
	else:
		return False


if __name__ == '__main__':
	download_file()
