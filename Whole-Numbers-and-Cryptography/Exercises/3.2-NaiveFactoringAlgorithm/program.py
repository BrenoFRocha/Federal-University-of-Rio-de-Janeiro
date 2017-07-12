def program():
	firstInput = raw_input("")
	counter = 0;
	while(int(counter) < int(firstInput)):
		counter += 1
		number1 = int(raw_input(""))
		initial = 2
		sameNumber = 0
		while(number1 != 1):
			if(number1 % initial == 0):
				number1 = number1/initial
				sameNumber += 1
				if(number1 % initial != 0):
					print(str(initial) + " " + str(sameNumber))
			if(number1 % initial != 0):
				sameNumber = 0
				initial += 1
			if(number1 == 1):
				print("---")
program()

