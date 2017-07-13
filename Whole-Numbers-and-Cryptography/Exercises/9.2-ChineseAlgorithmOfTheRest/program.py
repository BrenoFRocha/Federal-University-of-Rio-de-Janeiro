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
def program():
	repeat = int(raw_input())
	counter = 0
	while(counter < repeat):
		n, m = input()
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
			print(str(k)+" "+str(r))
			i += 1
		print("---")
		counter += 1
program()