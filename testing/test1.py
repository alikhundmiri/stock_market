from bsedata.bse import BSE
from pprint import pprint # just for neatness of display

b = BSE()
# print(b)
q = b.getQuote("500209")
pprint(q)