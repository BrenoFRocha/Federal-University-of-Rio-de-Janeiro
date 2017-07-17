def ListPhi(n):
	number = n
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
	return listD
def Groups(lista, number, original):
	l = lista
	n = number
	i = 0
	k = 0
	finalL = []
	while(i < len(l)):
		g = (n**i)%original
		j = 0
		k = 0
		while(k < len(finalL)):
			if(g == finalL[k]):
				return sorted(finalL)
			k += 1
		while(j < len(l)):
			if(g == l[j]):
				finalL.append(g)
			j += 1
		i += 1
	return sorted(finalL)
def program():
	repeat = int(raw_input(""))
	counter = 0;
	while(counter < repeat):
		number = input()
		listF = ListPhi(number)
		print(listF)
		i = 0
		while(i < len(listF)):
			print(Groups(listF, listF[i], number))
			i += 1
		counter += 1
program()