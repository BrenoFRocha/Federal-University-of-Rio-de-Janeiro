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
			return column2
def nFermat(n):
	numb = 2**(2**n)+1
	return numb
def program():
	repeat = raw_input("")
	counter = 0;
	while(int(counter) < int(repeat)):
		number = int(raw_input(""))
		v = nFermat(number)
		print(v)
		if(expmodular((v-1)/2, 5, v) == 1):
			print("PRIMO")
		else:
			print("COMPOSTO")
		print("---")
		counter += 1
program()