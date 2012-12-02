#!/usr/bin/env python

def hotelCost(days):
    return 140 * days

def planeRideCost(city):
    if city == "Charlotte" :
        return 183 
    if city == "Tampa" :
        return 220 
    if city == "Pittsburgh" : 
        return 222
    if city == "Los Angeles" :
        return 475

def rentalCarCost(days):
    cost = days * 40
    if days >= 7 :
        return cost - 50
    elif days >= 3 :
        return cost - 20
    else:
        return cost 
    
def tripCost(city, days, spendingMoney):
	total = spendingMoney + planeRideCost(city) + hotelCost(days) + rentalCarCost(days)
	print(total)
	return total
	
tripCost("Los Angeles", 5, 600)
