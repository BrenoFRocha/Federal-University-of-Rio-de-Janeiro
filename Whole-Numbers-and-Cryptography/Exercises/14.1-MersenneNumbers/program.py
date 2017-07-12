def fermat(n,b, m):
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
def mersenne(n):
	num = n
	num = (2**num)-1
	return num
def getR(n1):
	num1 = n1
	r = 0
	r = (int)(((2**num1)**0.5)/(2*num1))
	return r
def getQ(n1, erre):
	r = erre
	num1 = n1
	q = 0
	q = 1+2*r*num1
	return q
def program():
	repeat = (int)(raw_input(""))
	counter = 0
	while(counter < repeat):
		number = (int)(raw_input(""))
		print(mersenne(number))
		r = getR(number)
		print(r)
		if(r == 0):
			print(mersenne(number))
		else:
			tests = 1
			q = 0
			while(tests <= r):
				q = getQ(number, tests)
				print(tests)
				if(fermat(number, 2, q) ==  1):
					print(q)
					tests = r+1
				else:
					tests += 1
					if(tests == r+1):
						print(mersenne(number))
		print("---")
		counter += 1
program()