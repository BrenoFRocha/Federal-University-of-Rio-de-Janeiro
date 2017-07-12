def program():
	firstInput = raw_input("")
	counter = 0;
	while(int(counter) < int(firstInput)):
		counter += 1
		pairNumbers = ""
		number1 = 0;
		number2 = 0;
		pairNumbers = raw_input("")
		number1 = int(pairNumbers.partition(',')[0])
		if int(pairNumbers.partition(',')[2]) == 0:
			number2 = int(raw_input(""))
		else:
			number2 = int(pairNumbers.partition(',')[2])
		result1 = number1 + number2
		result2 = number1 - number2
		result3 = number1 * number2
		result4 = number1 / number2
		result5 = number1 % number2
		print(str(result1) + " " + str(result2) + " " + str(result3) + " " + str(result4) + " " + str(result5))
program()

