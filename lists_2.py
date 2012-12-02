groceries = {
    "banana": 1, 
    "orange": 2,
    "apple": 3
    }

stock = {"banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
    }
    
prices = {"banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
    }

def computeBill(qqq):
    total = 0
    for item in qqq:
        if stock[item] > 0:
            total += qqq[item] * prices[item]
            stock[item] -= groceries[item] 
            print stock[item]
    print total

computeBill(groceries)
