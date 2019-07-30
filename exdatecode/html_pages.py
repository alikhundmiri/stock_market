import os
import json
import glob
import codecs
import datetime
import webbrowser


from exdatecode.notify import notify
from exdatecode.file_and_folder_processing import BASE_DIR, get_latest_file

row_data = '''<div class="col-lg-4 col-md-6 mb-4">
	<div class="card h-100">
		<a href="#"><img class="card-img-top" src="http://placehold.it/700x400" alt=""></a>
		<div class="card-body">
			<h4 class="card-title">
				<a href="#">{company_name}</a>
			</h4>
			<h5>{incentive}</h5>
			<p class="card-text"> last date: {last_date}<br> date 2: {date_2}<br> date 3: {date_3}</p>
		</div>
		<div class="card-footer">
			<small class="text-muted"><a target='_blank' href='#'>View website</a></small>
		</div>
	</div>
</div>

'''
def html_page_manager(companies_list):
	print("Stage 03 | HTML Page Management")

	week_dir = get_latest_file()
	today_date = datetime.date.today().strftime('%d-%m-%Y')

	html_location  = '/Users/alikhundmiri/stockmarket/web_pages/{}.html'.format(today_date)

	# print(html_location)
	if os.path.exists(html_location):
		print('Stage 03 | HTML Page Management | File already exists...')
	else:
		print('Stage 03 | HTML Page Management | Generating HTML Page...')

		generate_html_page(companies_list, today_date, html_location)
	
	webbrowser.open(html_location)	
	return True



def generate_html_page(companies_list, today_date, html_location):
	json_data = json.dumps(companies_list)
	print('Stage 03 | HTML Page Management | Generating HTML Page... | fetching template')

	f=codecs.open("/Users/alikhundmiri/stockmarket/web_pages/product_sample.html", 'r')
	base_html = f.read()

	f.close()

	# print(today_date)
	filled_rows_snippet = ''' '''
	print('Stage 03 | HTML Page Management | Generating HTML Page... | collecting data')

	for company in companies_list:
		this_row_data = row_data.format(company_name=company[2], incentive=company[4], last_date=company[3], date_2=company[6], date_3=company[7])
		filled_rows_snippet = filled_rows_snippet + this_row_data

	print('Stage 03 | HTML Page Management | Generating HTML Page... | creating new page')

	updated_file = base_html.format(date=today_date, list_of_stocks=filled_rows_snippet)
	
	f = open(html_location,"w+")
	print('Stage 03 | HTML Page Management | Generating HTML Page... | writing new page')

	f.write(updated_file)
	f.close()

	# print(filled_rows_snippet)


	pass

def send_emails(html_content):
	pass