def program():
	firstInput = raw_input("")
	counter = 0
	original = 0
	nC = []
	total = 0
	i = 0
	while(int(counter) < int(firstInput)):
		number1 = int(raw_input(""))
		original = number1
		initial = 2
		sameNumber = 0
		while(number1 > 1):
			if(number1 % initial == 0):		
				if(sameNumber == 0):
					nC.append(initial);
				number1 = number1/initial
				sameNumber += 1
				if(number1 % initial != 0):
					print(str(initial) + " " + str(sameNumber))
			if(number1 % initial != 0):
				sameNumber = 0
				initial += 1
			if(number1 == 1):
				while(i < len(nC)):
					if((original-1)%(nC[i]-1) == 0 and ((nC[i]*nC[i])%original != 0)):
						total += 1
					i += 1
				if(total == len(nC)):
					print("SIM")
				else:
					print("NAO")
				print("---")
		total = 0
		nC = []
		i = 0
		counter += 1	
program()

