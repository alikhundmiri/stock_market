from selenium import webdriver
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
from notify import notify

url = 'https://www.bseindia.com/corporates/corporate_act.aspx'


def launch_chrome():
	global driver
	print("Launching Chrome...")
	notify("Launching Chrome...", "Attempting to download Corporate Act", None)
	driver = webdriver.Chrome('/Library/SeleniumWebDrivers/WebDrivers/chromedriver')
	time.sleep(1)


def open_website(page_link):
	#open page
	driver.get(page_link)

	assert "BSEINDIA" in driver.title
	print("Website is open!")

	download_button = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_lnkDownload1"]')
	print("Attempting to Downloading file...")

	download_button.click()
	print("download started...")
	return driver

def check_download(driver):
	if not driver.current_url.startswith("chrome://downloads"):
		driver.get("chrome://downloads/")

	last_download = driver.find_element_by_xpath('//*[@id="file-link"]')
	print(last_download.text)
	

def download_file():
	launch_chrome()
	open_website(url)
	# waits for all the files to be completed and returns the paths
	check_download(driver)
	
	driver.close()
if __name__ == '__main__':
	download_file()
