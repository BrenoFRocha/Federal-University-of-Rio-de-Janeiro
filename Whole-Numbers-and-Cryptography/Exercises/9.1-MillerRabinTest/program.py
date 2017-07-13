def ExpModular(b,e,m):
	result = 1
	base = b
	exponent = e
	module = m
	if(exponent % 2 == 0):
		print(str(result) + " " + str(base) + " "+ str(exponent) + " N")
	else:
		print(str(result) + " " + str(base) + " "+ str(exponent) + " S")
	while(exponent != 0):
		if(exponent % 2 == 0):
			exponent /= 2
			base *= base
			base = base%module
			if(exponent % 2 == 0):
				print(str(result) + " " + str(base) + " "+ str(exponent) + " N")
			else:
				print(str(result) + " " + str(base) + " "+ str(exponent) + " S")
		else:
			exponent = (exponent-1)/2
			result = (result*base)%module
			base *= base
			base = base%module
			if(exponent % 2 == 0):
				print(str(result) + " " + str(base) + " "+ str(exponent) + " N")
			else:
				print(str(result) + " " + str(base) + " "+ str(exponent) + " S")
	return result
def MillerRabin(n,b):
	k = 0
	q = n-1
	while(q % 2 == 0):
		k += 1
		q /= 2
	print(str(k) + " " + str(q))
	t = ExpModular(b,q,n)
	if(t == 1 or t == n-1):
		return "INCONCLUSIVO"
	i = 1
	print(str(q)+" "+str(t))
	while(i < k):
		q *= 2
		t = (t*t)%n
		print(str(q)+" "+str(t))
		if(t == n-1):
			return "INCONCLUSIVO"
		i += 1
	return "COMPOSTO"
def program():
	repeat = int(raw_input(""))
	counter = 0
	while(counter < repeat):
		pairNumbers = raw_input("")
		n = int(pairNumbers.split(",")[0])
		b = int(pairNumbers.split(",")[1])
		print(MillerRabin(n,b))
		print("---")
		counter += 1
program()