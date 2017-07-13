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
			savedY = y1
	return savedX, savedY
def chinese(l1,l2):
	n = l1
	m = l2
	i = 0
	r = m[i]
	k = n[i]
	while(i < len(m) - 1):
		x, y = euclidiano(r, m[i+1])
		temp = k
		k = (n[i+1] - (k%m[i+1]))
		k = (k*x)%m[i+1]
		k *= r
		k += temp
		print(str(x) + " " + str(y))
		r *= m[i+1]
		print(str(k) + " " + str(r))
		i += 1
def fermatexp(b,e,m):
	number1 = b
	number2 = e
	number3 = m
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
	return column1
def ingenuo(n):
	number = n
	initial = 2
	sameNumber = 0
	L = []
	while(number != 1):
		if(number % initial == 0):
			number = number/initial
			sameNumber += 1
			if(number % initial != 0):
				print(str(initial) + " " + str(sameNumber))
				L.append(initial)
		if(number % initial != 0):
			sameNumber = 0
			initial += 1
	return L
def program():
	repeat = int(raw_input())
	counter = 0
	while(counter < repeat):
		pairNumbers = raw_input("")
		n1 = int(pairNumbers.split(",")[0])
		n2 = int(pairNumbers.split(",")[1])
		n3 = int(pairNumbers.split(",")[2])	
		L = []
		L = ingenuo(n3)
		X = []
		i = 0
		qt = len(L)
		while(i < qt):
			if(n1%L[i] == 0):
				X.append(0)
				print("0")
			else:
				X.append(fermatexp(n1, n2, L[i]))
			i += 1
		print(len(X))
		print(len(L))
		chinese(X,L)
		print("---")
		counter += 1
program()