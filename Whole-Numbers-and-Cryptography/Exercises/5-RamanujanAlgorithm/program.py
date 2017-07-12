def program():
	numberMAX = int(raw_input(""))
	number = 2
	initial = 1
	tempQuant = 0
	quant = 0
	dlist = [1]
	while(number <= numberMAX):
		while(initial <= number):
			temp = number%initial
			if(temp == 0):
				quant += 1
			if(initial == number and tempQuant < quant):
					tempQuant = quant
					dlist.append(number)
			initial += 1
		quant = 0
		initial = 1
		if(number >= 45360):
			number += 5040
		elif(number >= 2520):
			number += 2520
		elif(number >= 840):
			number += 420
		elif(number >= 60):
			number += 60
		elif(number >= 12):
			number += 12
		else:
			number += 2	
	print(dlist)
program()