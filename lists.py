prices = {
	"banana": 4,
	"apple": 2,
	"orange": 1.5,
	"pear": 3
	}

stock = {
	"banana": 6,
	"apple": 0,
	"orange": 32,
	"pear": 15
	}

for key in stock.keys():
    if stock[key] > 0 :
        print key
        print "price: " + str(prices[key])
        print "stock: " + str(stock[key])
        print

sum = 0

for key in prices.keys():
    sum += prices[key] * stock[key]

print "Total: " + str(sum)

