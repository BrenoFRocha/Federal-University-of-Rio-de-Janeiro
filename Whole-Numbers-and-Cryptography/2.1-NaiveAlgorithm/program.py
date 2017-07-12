def program():
	firstInput = raw_input("")
	counter = 0;
	while(int(counter) < int(firstInput)):
		counter += 1
		pairNumbers = ""
		number1 = 0;
		number2 = 0;
		quociente = 0;
		resto = 0;
		pairNumbers = raw_input("")
		number1 = int(pairNumbers.partition(',')[0])
		if int(pairNumbers.partition(',')[2]) == 0:
			number2 = int(raw_input(""))
		else:
			number2 = int(pairNumbers.partition(',')[2])
		print("0 " + str(number1))
		while(number1 > number2):
			quociente += 1
			number1 -= number2
			print(str(quociente) +" " + str(number1))
			if(number1 <= number2):
				print("---")
program()

