def ingenuo(n):
	number = n
	initial = 2
	sameNumber = 0
	quantN = [1]
	while(number != 1):
		if(number % initial == 0):
			number = number/initial
			sameNumber += 1
			if(number % initial != 0):
				print(str(initial) + " " + str(sameNumber))
				quantN.append(initial)
		if(number % initial != 0):
			sameNumber = 0
			initial += 1
		if(number == 1):
			return quantN;
def expmodular(n,b, m):
	number3 = m
	column1 = 1
	column2 = b
	column3 = n
	if(column3 % 2 == 0):
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
			return column1
def program():
	repeat = raw_input("")
	counter = 0;
	while(int(counter) < int(repeat)):
		number = int(raw_input(""))
		listNI = []
		listNI = ingenuo(number - 1)
		countT = 0
		b = 2
		result = []
		print(b)
		if(expmodular(number-1,b,number) != 1):
			print("COMPOSTO")
		else:
			while(countT < len(listNI)):
				n1 = (number-1)/listNI[countT]
				print(n1)
				g = expmodular(n1, b, number)
				result.append(g)
				countT += 1
				if(result[countT -1] == 1 and countT != 1):
					countT = 0
					result = []
					b += 1
					if(b != number):
						print(b)
				elif(result[countT-1] != 1 and countT == 1 and b < number):
					countT = 0
					result = []
					b += 1
					if(b != number):
						print(b)
				if(b == number):
					countT = len(listNI)
					print("COMPOSTO")
				elif(countT == len(listNI)):
					countT = len(listNI)
					print("PRIMO")
		print("---")
		counter += 1
program()