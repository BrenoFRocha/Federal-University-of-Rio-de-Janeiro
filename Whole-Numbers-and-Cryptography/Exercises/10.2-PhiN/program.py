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
		auxMN = number
		auxMD = 2
		auxQ = 0
		while(auxMN != 1):
			if(auxMN % auxMD == 0):
				auxMN = auxMN/auxMD
				auxQ += 1
				if(auxMN == 1):
					print(str(auxMD) +" "+ str(auxQ))
			else:
				if(auxQ != 0):
					print(str(auxMD) +" "+ str(auxQ))
					auxQ = 0
				auxMD += 1
		while(divisor < number):
			auxN = number #8
			auxD = divisor #1
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
		print(len(listD))
		print("---")
		counter += 1
program()

