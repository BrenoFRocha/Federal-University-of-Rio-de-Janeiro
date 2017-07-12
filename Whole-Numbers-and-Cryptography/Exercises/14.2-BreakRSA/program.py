def phi(n):
	number = n
	listD = []
	divisor = 1
	auxN = 0
	auxD = 0
	resto = 0
	while(divisor < number):
		auxN = number 
		auxD = divisor 
		resto = 1
		while(resto != 0):
			resto = auxN%auxD
			if(resto == 0):
				if(auxD == 1):
					listD.append(divisor)
				divisor += 1
			else:
				auxN = auxD
				auxD = resto
	return len(listD)
def fermat(n):
	number = n
	x = (int)(number ** 0.5)
	y = 0
	print(str(x) + " " + str(y) + " N")
	while(number != ((x**2) - (y**2))):
		x += 1
		y = (int)(((x**2) - number) ** 0.5) 
		if(number != ((x**2) - (y**2))):
			print(str(x) + " " + str(y) + " N")
		else:
			if(x + y == number):
				print(str(x) + " " + str(y) + " N")
			else:
				print(str(x) + " " + str(y) + " S")
			print(str(x-y) + " " + str(x+y))
def euclidiano(n1,n2):
	number1 = 0
	number2 = 0
	quociente = 0
	resto = 0
	savedX = 0
	x1 = 1
	x2 = 0
	y1 = 0
	y2 = 1
	number1 = n1
	number2 = n2
	originalNumber = number2;
	print(str(number1) + " - 1 0")
	print(str(number2) + " - 0 1")
	while(number2 != 0):
		if(originalNumber == number2):
			temp = y2
			temp -= y1 * quociente
			y2 = y1
			y1 = temp 	
		resto = number1 % number2
		quociente = number1/number2
		temp = y2
		temp -= y1 * quociente
		y2 = y1
		y1 = temp 	
		number1 = number2
		number2 = resto
		temp = x1
		temp -= x2 * quociente
		x1 = x2
		x2 = temp
		if(number2 == 0):
			print(str(number2) + " " + str(quociente) +  " - - ")
		else:
			print(str(number2) + " " + str(quociente) +  " " + str(x2) + " " + str(y1))
			savedX = x2
	return savedX
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
			print(column1)
def modulo(n1,n2):
	mod = 0
	num1 = n1
	num2 = n2
	if(num1 < 0):
		num1 *= -1
		if(num1 < num2):
			mod = num2 - num1
		else:
			mod = num2%num1
	else:
		mod = num2%num1
	return mod
def program():
	repeat = (int)(raw_input(""))
	counter = 0
	while(counter < repeat):
		number, e, b = input()
		sX = 0
		fermat(number)
		print(phi(number))
		sX = euclidiano(e, phi(number))
		print(modulo(sX, phi(number)))
		expmodular(modulo(sX, phi(number)), b, number)
		print("---")
		counter += 1
program()