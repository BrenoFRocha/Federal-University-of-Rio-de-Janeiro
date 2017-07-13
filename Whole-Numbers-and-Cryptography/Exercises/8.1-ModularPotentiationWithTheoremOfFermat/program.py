def program():
	repeat = int(raw_input(""))
	counter = 0
	number1 = 0
	number2 = 0
	number3 = 0
	while(counter < repeat):
		pairNumbers = raw_input("")
		number1 = int(pairNumbers.split(",")[0])
		number2 = int(pairNumbers.split(",")[1])
		number3 = int(pairNumbers.split(",")[2])	
		column1 = 1
		column2 = number1
		column3 = number2%(number3-1)
		print(column3)
		if(number2 % 2 == 0):
			print(str(column1) + " " + str(column2) + " " + str(column3) + " " + "N")
		else:
			print(str(column1) + " " + str(column2) + " " + str(column3) + " " + "S")
		while(column3 != 0):
			if(column3 % 2 == 0):
				column3 /= 2
				column2 *= column2
				column2 = column2%number3
			else:
				column3 = (column3-1)/2
				column1= (column1*column2)%number3
				column2 *= column2
				column2 = column2%number3
			if(column3 % 2 == 0):
				print(str(column1) + " " + str(column2) + " " + str(column3) + " " + "N")
			else:
				print(str(column1) + " " + str(column2) + " " + str(column3) + " " + "S")
			if(column3 == 0):
				print("---")
		counter += 1
program()