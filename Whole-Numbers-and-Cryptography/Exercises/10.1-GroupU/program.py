def program():
	repeat = int(raw_input(""))
	counter = 0;
	while(counter < repeat):
		number = int(raw_input(""))
		listD = []
		divisor = 1
		auxN = 0
		auxD = 0
		resto = 0
		while(divisor < number):
			auxN = number 
			auxD = divisor 
			resto = 1
			while(resto != 0):
				resto = auxN%auxD
				if(resto == 0):
					if(auxD == 1):
						listD.append(divisor)
					divisor += 1
				else:
					auxN = auxD
					auxD = resto
		print(listD)
		counter += 1
program()

