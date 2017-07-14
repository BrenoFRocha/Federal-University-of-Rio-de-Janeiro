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

def TestG(lista, n, original):
	i = 0
	result = False
	while(i < len(lista)):
		g = (n*lista[i])%original
		k = 0
		f = False
		while(k < len(lista)):
			if(g == lista[k]):
				f = True
			k += 1
		if(f == False):
			result = True
		i += 1
	return result



def program():
	repeat = int(raw_input(""))
	counter = 0;
	while(counter < repeat):
		number, listC = input()
		listF = ListPhi(number)
		t = 0
		yorn = True
		while(t < len(listC)):
			if(TestG(listC, listC[t], number)):
				yorn = False
			t += 1 
		if(yorn):
			print("SIM")
		else: 
			print("NAO")
		counter += 1
program()

