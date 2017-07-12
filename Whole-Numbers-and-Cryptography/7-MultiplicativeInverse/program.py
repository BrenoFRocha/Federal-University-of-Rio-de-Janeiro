def program():
	firstInput = raw_input("")
	counter = 0
	while(int(counter) < int(firstInput)):
		counter += 1
		pairNumbers = ""
		number1 = 0
		number2 = 0
		quociente = 0
		resto = 0
		x1 = 1
		x2 = 0
		y1 = 0
		y2 = 1
		pairNumbers = raw_input("")
		number1 = int(pairNumbers.partition(',')[0])
		number2 = int(pairNumbers.partition(',')[2])
		MDC = 0
		savedN2 = number2
		savedX = 0
		originalNumber = number2
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
				if(MDC == 1):
					if(savedX < 0):
						savedX = savedN2 + savedX
					print(str(savedX))
				else:
					print("0")
				print("---")
			else:
				print(str(number2) + " " + str(quociente) +  " " + str(x2) + " " + str(y1))
				MDC = number2;
				savedX = x2
program()