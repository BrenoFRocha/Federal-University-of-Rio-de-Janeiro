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
	return column1

def program():
	repeat = (int)(raw_input(""))
	counter = 0
	while(counter < repeat):
		p, a, s, t = input()
		chave = expmodular(p-a-1, s, p);
		chave = (chave*t)%p
		print(chave)
		print("---")
		counter += 1
program()
