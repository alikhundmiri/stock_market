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