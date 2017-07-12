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
	originalNumber = number2
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
		if(number2 != 0):
			savedX = x2			
	return savedX
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
def expmodular(n,b, m):
	number3 = m
	column1 = 1
	column2 = b
	column3 = n
	
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
	return column1
def program():
	repeat = int(raw_input(""))
	counter = 0;
	while(counter < repeat):
		g, h, p = input()
		k = p-1
		m = int((k**0.5)+1)
		print(m)
		j = 0
		listJ = []
		while(j < m):
			temp = g
			temp = (temp**j)%p
			listJ.append(temp)
			print(str(j)+" "+str(temp))
			j += 1
		t = euclidiano(g, p)
		t = modulo(t, p)
		t = expmodular(m,t,p)
		i = 0
		find = False
		while(i < t and find == False):
			temp = (h*(t**i))%p
			verify = 0
			while(verify < len(listJ)):
				if(listJ[verify] == temp):
					find = True
					dJ = verify
					dI = i
					verify = len(listJ)
				else:
					verify += 1
			print(str(i) + " " + str(temp))
			i += 1
		print(str(dI) + " " + str(dJ))
		x = dI*m+dJ
		print(x)
		print("---")
		counter += 1
program()