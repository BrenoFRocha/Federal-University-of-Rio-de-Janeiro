def program():
	repeat = int(raw_input(""))
	counter = 0
	number1 = 0
	number2 = 0
	number3 = 0
	while(counter < repeat):
		counter += 1
		pairNumbers = raw_input("")
		number1 = int(pairNumbers.split(",")[0])
		number2 = int(pairNumbers.split(",")[1])
		number3 = int(pairNumbers.split(",")[2])	
		column1 = number1 % number3 
		column2 = number2 % number3 
		column3 = (number1 + number2) % number3
		column4 = (number1 - number2) % number3
		column5 = (number1 * number2) % number3
		print(str(column1) + " " + str(column2) + " " + str(column3) + " " + str(column4) + " " + str(column5))
program()