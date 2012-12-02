def factory(number):
	if number == 1:
		return 1
	else:
		return number*factory(number-1) 
print factory(5)
