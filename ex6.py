# from sys import argv
# script, name = argv

def dbBase():
	db = {}
	db['amazon'] = 100
	db['ebay'] = 80
	db['wallmart'] = 60
	return db

def Order(item, argDB):
	print 'item: ', item
	for price in argDB:
		print price, "price: ", argDB[price]
		
Order('computer', dbBase())






