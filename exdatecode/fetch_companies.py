import json
import requests
from bs4 import BeautifulSoup

url = 'https://www.bseindia.com/corporates/corporate_act.aspx'

html_data = '''
</table></td>
</tr><tr class="innertable_header">
<th scope="col">Security Code</th><th scope="col">Security Name</th><th scope="col">Ex Date</th><th scope="col">Purpose</th><th scope="col">Record Date</th><th scope="col">BC Start Date</th><th scope="col">BC End Date</th><th scope="col">ND Start Date</th><th scope="col">ND End Date</th><th scope="col">Actual Payment Date</th>
</tr><tr class="TTRow">
<td><a class="tablebluelink" href="ScripWiseCorpAction.aspx?scrip_cd=500215">500215</a></td><td class="TTRow_left">ATFL</td><td width="50">08 Jul 2019</td><td class="TTRow_left">Dividend - Rs. - 2.5000</td><td>-</td><td width="50">10 Jul 2019</td><td width="50">17 Jul 2019</td><td>03 Jul 2019</td><td>09 Jul 2019</td><td>
<span id="ContentPlaceHolder1_gvData_paymentdate_0" style="display:inline-block;" wrap="false">-</span>
</td>
</tr><tr class="TTRow">
<td><a class="tablebluelink" href="ScripWiseCorpAction.aspx?scrip_cd=533047">533047</a></td><td class="TTRow_left">IMFA</td><td width="50">08 Jul 2019</td><td class="TTRow_left">Dividend - Rs. - 5.0000</td><td>-</td><td width="50">10 Jul 2019</td><td width="50">17 Jul 2019</td><td>03 Jul 2019</td><td>09 Jul 2019</td><td>
<span id="ContentPlaceHolder1_gvData_paymentdate_1" style="display:inline-block;" wrap="false">-</span>
</td>
</tr><tr class="TTRow">
<td><a class="tablebluelink" href="ScripWiseCorpAction.aspx?scrip_cd=500228">500228</a></td><td class="TTRow_left">JSWSTEEL</td><td width="50">08 Jul 2019</td><td class="TTRow_left">Dividend - Rs. - 4.1000</td><td>-</td><td width="50">10 Jul 2019</td><td width="50">12 Jul 2019</td><td>03 Jul 2019</td><td>09 Jul 2019</td><td>
<span id="ContentPlaceHolder1_gvData_paymentdate_2" style="display:inline-block;" wrap="false">-</span>
</td>
</tr><tr class="TTRow">
<td><a class="tablebluelink" href="ScripWiseCorpAction.aspx?scrip_cd=532819">532819</a></td><td class="TTRow_left">MINDTREE</td><td width="50">08 Jul 2019</td><td class="TTRow_left">Final Dividend - Rs. - 4.0000</td><td>-</td><td width="50">10 Jul 2019</td><td width="50">16 Jul 2019</td><td>03 Jul 2019</td><td>09 Jul 2019</td><td>
<span id="ContentPlaceHolder1_gvData_paymentdate_3" style="display:inline-block;" wrap="false">-</span>
</td>
</tr><tr class="TTRow">
<td><a class="tablebluelink" href="ScripWiseCorpAction.aspx?scrip_cd=532819">532819</a></td><td class="TTRow_left">MINDTREE</td><td width="50">08 Jul 2019</td><td class="TTRow_left">Special Dividend - Rs. - 20.0000</td><td>-</td><td width="50">10 Jul 2019</td><td width="50">16 Jul 2019</td><td>03 Jul 2019</td><td>09 Jul 2019</td><td>
<span id="ContentPlaceHolder1_gvData_paymentdate_4" style="display:inline-block;" wrap="false">-</span>
</td>
</tr><tr class="TTRow">
<td><a class="tablebluelink" href="ScripWiseCorpAction.aspx?scrip_cd=505807">505807</a></td><td class="TTRow_left">ROLCOEN</td><td width="50">08 Jul 2019</td><td class="TTRow_left">Dividend - Rs. - 1.5000</td><td>-</td><td width="50">10 Jul 2019</td><td width="50">16 Jul 2019</td><td>03 Jul 2019</td><td>09 Jul 2019</td><td>
<span id="ContentPlaceHolder1_gvData_paymentdate_5" style="display:inline-block;" wrap="false">-</span>
</td>
</tr><tr class="TTRow">
<td><a class="tablebluelink" href="ScripWiseCorpAction.aspx?scrip_cd=500405">500405</a></td><td class="TTRow_left">SUPPETRO</td><td width="50">08 Jul 2019</td><td class="TTRow_left">Final Dividend - Rs. - 2.0000</td><td>-</td><td width="50">10 Jul 2019</td><td width="50">12 Jul 2019</td><td>03 Jul 2019</td><td>09 Jul 2019</td><td>
<span id="ContentPlaceHolder1_gvData_paymentdate_6" style="display:inline-block;" wrap="false">-</span>
</td>
</tr><tr class="TTRow">
<td><a class="tablebluelink" href="ScripWiseCorpAction.aspx?scrip_cd=500408">500408</a></td><td class="TTRow_left">TATAELXSI</td><td width="50">08 Jul 2019</td><td class="TTRow_left">Dividend - Rs. - 13.5000</td><td>-</td><td width="50">10 Jul 2019</td><td width="50">17 Jul 2019</td><td>03 Jul 2019</td><td>09 Jul 2019</td><td>
<span id="ContentPlaceHolder1_gvData_paymentdate_7" style="display:inline-block;" wrap="false">-</span>
</td>
</tr><tr class="TTRow">
<td><a class="tablebluelink" href="ScripWiseCorpAction.aspx?scrip_cd=540762">540762</a></td><td class="TTRow_left">TIINDIA</td><td width="50">08 Jul 2019</td><td class="TTRow_left">Final Dividend - Rs. - 0.7500</td><td>-</td><td width="50">10 Jul 2019</td><td width="50">24 Jul 2019</td><td>03 Jul 2019</td><td>09 Jul 2019</td><td>
<span id="ContentPlaceHolder1_gvData_paymentdate_8" style="display:inline-block;" wrap="false">-</span>
</td>
</tr><tr class="TTRow">
<td><a class="tablebluelink" href="ScripWiseCorpAction.aspx?scrip_cd=511196">511196</a></td><td class="TTRow_left">CANFINHOME</td><td width="50">09 Jul 2019</td><td class="TTRow_left">Dividend - Rs. - 2.0000</td><td>-</td><td width="50">11 Jul 2019</td><td width="50">17 Jul 2019</td><td>04 Jul 2019</td><td>10 Jul 2019</td><td>
<span id="ContentPlaceHolder1_gvData_paymentdate_9" style="display:inline-block;" wrap="false">-</span>
</td>
</tr><tr class="TTRow">
<td><a class="tablebluelink" href="ScripWiseCorpAction.aspx?scrip_cd=532155">532155</a></td><td class="TTRow_left">GAIL</td><td width="50">09 Jul 2019</td><td class="TTRow_left">Bonus issue 1:1</td><td>10 Jul 2019</td><td width="50"> </td><td width="50"> </td><td>03 Jul 2019</td><td>09 Jul 2019</td><td>
<span id="ContentPlaceHolder1_gvData_paymentdate_10" style="display:inline-block;" wrap="false">-</span>
</td>
</tr><tr class="TTRow">
<td><a class="tablebluelink" href="ScripWiseCorpAction.aspx?scrip_cd=511288">511288</a></td><td class="TTRow_left">GRUH</td><td width="50">09 Jul 2019</td><td class="TTRow_left">Dividend - Rs. - 2.0000</td><td>-</td><td width="50">11 Jul 2019</td><td width="50">19 Jul 2019</td><td>04 Jul 2019</td><td>10 Jul 2019</td><td>
<span id="ContentPlaceHolder1_gvData_paymentdate_11" style="display:inline-block;" wrap="false">-</span>
</td>
</tr><tr class="TTRow">
<td><a class="tablebluelink" href="ScripWiseCorpAction.aspx?scrip_cd=540133">540133</a></td><td class="TTRow_left">ICICIPRULI</td><td width="50">09 Jul 2019</td><td class="TTRow_left">Final Dividend - Rs. - 1.5500</td><td>-</td><td width="50">11 Jul 2019</td><td width="50">17 Jul 2019</td><td>04 Jul 2019</td><td>10 Jul 2019</td><td>
<span id="ContentPlaceHolder1_gvData_paymentdate_12" style="display:inline-block;" wrap="false">-</span>
</td>
</tr><tr class="TTRow">
<td><a class="tablebluelink" href="ScripWiseCorpAction.aspx?scrip_cd=532218">532218</a></td><td class="TTRow_left">SOUTHBANK</td><td width="50">09 Jul 2019</td><td class="TTRow_left">Dividend - Rs. - 0.2500</td><td>-</td><td width="50">11 Jul 2019</td><td width="50">17 Jul 2019</td><td>04 Jul 2019</td><td>10 Jul 2019</td><td>
<span id="ContentPlaceHolder1_gvData_paymentdate_13" style="display:inline-block;" wrap="false">-</span>
</td>
</tr><tr class="TTRow">
<td><a class="tablebluelink" href="ScripWiseCorpAction.aspx?scrip_cd=506285">506285</a></td><td class="TTRow_left">BAYERCROP</td><td width="50">10 Jul 2019</td><td class="TTRow_left">Final Dividend - Rs. - 18.0000</td><td>-</td><td width="50">12 Jul 2019</td><td width="50">24 Jul 2019</td><td>05 Jul 2019</td><td>11 Jul 2019</td><td>
<span id="ContentPlaceHolder1_gvData_paymentdate_14" style="display:inline-block;" wrap="false">-</span>
</td>
</tr><tr class="TTRow">
<td><a class="tablebluelink" href="ScripWiseCorpAction.aspx?scrip_cd=506395">506395</a></td><td class="TTRow_left">COROMANDEL</td><td width="50">10 Jul 2019</td><td class="TTRow_left">Final Dividend - Rs. - 3.5000</td><td>-</td><td width="50">12 Jul 2019</td><td width="50">22 Jul 2019</td><td>05 Jul 2019</td><td>11 Jul 2019</td><td>
<span id="ContentPlaceHolder1_gvData_paymentdate_15" style="display:inline-block;" wrap="false">-</span>
</td>
</tr><tr class="TTRow">
<td><a class="tablebluelink" href="ScripWiseCorpAction.aspx?scrip_cd=540000">540000</a></td><td class="TTRow_left">D46SM36DG</td><td width="50">10 Jul 2019</td><td class="TTRow_left">Redemption of Mutual Fund </td><td>11 Jul 2019</td><td width="50"> </td><td width="50"> </td><td>04 Jul 2019</td><td>10 Jul 2019</td><td>
<span id="ContentPlaceHolder1_gvData_paymentdate_16" style="display:inline-block;" wrap="false">-</span>
</td>
</tr><tr class="TTRow">
<td><a class="tablebluelink" href="ScripWiseCorpAction.aspx?scrip_cd=539999">539999</a></td><td class="TTRow_left">D46SM36RD</td><td width="50">10 Jul 2019</td><td class="TTRow_left">Redemption of Mutual Fund </td><td>11 Jul 2019</td><td width="50"> </td><td width="50"> </td><td>04 Jul 2019</td><td>10 Jul 2019</td><td>
<span id="ContentPlaceHolder1_gvData_paymentdate_17" style="display:inline-block;" wrap="false">-</span>
</td>
</tr><tr class="TTRow">
<td><a class="tablebluelink" href="ScripWiseCorpAction.aspx?scrip_cd=539998">539998</a></td><td class="TTRow_left">D46SM36RG</td><td width="50">10 Jul 2019</td><td class="TTRow_left">Redemption of Mutual Fund </td><td>11 Jul 2019</td><td width="50"> </td><td width="50"> </td><td>04 Jul 2019</td><td>10 Jul 2019</td><td>
<span id="ContentPlaceHolder1_gvData_paymentdate_18" style="display:inline-block;" wrap="false">-</span>
</td>
</tr><tr class="TTRow">
<td><a class="tablebluelink" href="ScripWiseCorpAction.aspx?scrip_cd=590003">590003</a></td><td class="TTRow_left">KARURVYSYA</td><td width="50">10 Jul 2019</td><td class="TTRow_left">Dividend - Rs. - 0.6000</td><td>-</td><td width="50">12 Jul 2019</td><td width="50">18 Jul 2019</td><td>05 Jul 2019</td><td>11 Jul 2019</td><td>
<span id="ContentPlaceHolder1_gvData_paymentdate_19" style="display:inline-block;" wrap="false">-</span>
</td>
</tr><tr class="TTRow">
<td><a class="tablebluelink" href="ScripWiseCorpAction.aspx?scrip_cd=500250">500250</a></td><td class="TTRow_left">LGBBROSLTD</td><td width="50">10 Jul 2019</td><td class="TTRow_left">Dividend - Rs. - 5.0000</td><td>-</td><td width="50">12 Jul 2019</td><td width="50">18 Jul 2019</td><td>05 Jul 2019</td><td>11 Jul 2019</td><td>
<span id="ContentPlaceHolder1_gvData_paymentdate_20" style="display:inline-block;" wrap="false">-</span>
</td>
</tr><tr class="TTRow">
<td><a class="tablebluelink" href="ScripWiseCorpAction.aspx?scrip_cd=502420">502420</a></td><td class="TTRow_left">ORIENTPPR</td><td width="50">10 Jul 2019</td><td class="TTRow_left">Final Dividend - Rs. - 0.6000</td><td>-</td><td width="50">12 Jul 2019</td><td width="50">19 Jul 2019</td><td>05 Jul 2019</td><td>11 Jul 2019</td><td>
<span id="ContentPlaceHolder1_gvData_paymentdate_21" style="display:inline-block;" wrap="false">-</span>
</td>
</tr><tr class="TTRow">
<td><a class="tablebluelink" href="ScripWiseCorpAction.aspx?scrip_cd=526492">526492</a></td><td class="TTRow_left">RISHIROOP</td><td width="50">10 Jul 2019</td><td class="TTRow_left">Final Dividend - Rs. - 1.2000</td><td>-</td><td width="50">12 Jul 2019</td><td width="50">18 Jul 2019</td><td>05 Jul 2019</td><td>11 Jul 2019</td><td>
<span id="ContentPlaceHolder1_gvData_paymentdate_22" style="display:inline-block;" wrap="false">-</span>
</td>
</tr><tr class="TTRow">
<td><a class="tablebluelink" href="ScripWiseCorpAction.aspx?scrip_cd=541556">541556</a></td><td class="TTRow_left">RITES</td><td width="50">10 Jul 2019</td><td class="TTRow_left">Final Dividend - Rs. - 4.0000</td><td>11 Jul 2019</td><td width="50"> </td><td width="50"> </td><td>04 Jul 2019</td><td>10 Jul 2019</td><td>
<span id="ContentPlaceHolder1_gvData_paymentdate_23" style="display:inline-block;" wrap="false">-</span>
</td>
</tr><tr class="TTRow">
<td><a class="tablebluelink" href="ScripWiseCorpAction.aspx?scrip_cd=532538">532538</a></td><td class="TTRow_left">ULTRACEMCO</td><td width="50">10 Jul 2019</td><td class="TTRow_left">Dividend - Rs. - 11.5000</td><td>-</td><td width="50">12 Jul 2019</td><td width="50">18 Jul 2019</td><td>05 Jul 2019</td><td>11 Jul 2019</td><td>
<span id="ContentPlaceHolder1_gvData_paymentdate_24" style="display:inline-block;" wrap="false">-</span>
</td>
</tr><tr class="pgr">
<td colspan="10"><table>
<tr>
<td><span>1</span></td><td><a href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$gvData','Page$2')">2</a></td><td><a href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$gvData','Page$3')">3</a></td><td><a href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$gvData','Page$4')">4</a></td><td><a href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$gvData','Page$5')">5</a></td><td><a href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$gvData','Page$6')">6</a></td><td><a href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$gvData','Page$7')">7</a></td><td><a href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$gvData','Page$8')">8</a></td><td><a href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$gvData','Page$9')">9</a></td><td><a href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$gvData','Page$10')">10</a></td><td><a href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$gvData','Page$11')">...</a></td><td><a href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$gvData','Page$Last')">Last</a></td>
</tr>
</table></td>
</tr>
</table>
'''
def get_list():
	page = requests.get(url)
	# print(page.text)
	soup = BeautifulSoup(page.text, 'html.parser')
	# print(soup.prettify())

	# companies = soup.find_all("tr", class_="TTRow")

	# for company in companies:
	# 	print(company.get_text())
		# print("\n")

	dividend_table = soup.find('table', class_='mGrid')
	# print(dividend_table)
	print("Type simple: {}".format(type(dividend_table)))
	print("Type .text : {}".format(type(dividend_table.text)))
	print("Type html_data : {}".format(type(html_data)))

	# dividend_table_text = dividend_table.text
	# table_data = [[cell.text for cell in row("td")]for row in BeautifulSoup(dividend_table_text)("tr")]

	# print(json.dumps(dict(table_data)))
	# print(table_data)

if __name__ == '__main__':
	get_list()