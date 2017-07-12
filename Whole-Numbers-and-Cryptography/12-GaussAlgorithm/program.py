def ingenuo(n1):
	number1 = (n1 - 1)
	initial = 2
	sameNumber = 0
	numbers = []
	expoents = []
	while(number1 != 1):
		if(number1 % initial == 0):
			number1 = number1/initial
			sameNumber += 1
			if(number1 % initial != 0):
				numbers.append(initial)
				expoents.append(sameNumber)
				print(str(initial) + " " + str(sameNumber))
		if(number1 % initial != 0):
			sameNumber = 0
			initial += 1
		if(number1 == 1):
			return numbers,expoents
def euclidiano(n1,n2):
	quociente = 0
	resto = 0
	number1 = n1
	number2 = n2
	while(number2 != 0):
		resto = number1 % number2
		quociente = number1/number2
		number1 = number2
		number2 = resto
		if(number2 == 0):
			return number1
def cicle(resultG, original):
	m = 1
	originalN = original
	g = resultG
	cicleN = []
	while(m < originalN-1):
		if(euclidiano(m, originalN-1) == 1):
			temp = (g**m)%originalN
			cicleN.append(int(temp))
		m += 1
	cicleN.sort()
	print(cicleN)
def gauss(nums, exps, n1):
	originalN = n1
	numbers = nums
	expoents = exps
	i = 0
	g = 1
	k = len(numbers)
	while(i < k):
		a = 2
		while((a ** ((originalN-1)/numbers[i]))%originalN == 1):
			a += 1 

		h = (a ** ((originalN-1)/(numbers[i] ** expoents[i])))%originalN
		g = (g*h)%originalN
		print (str(numbers[i]) + " " + str(a) + " " + str(h))
		i += 1
	print(g)
	cicle(g, n1)
	print("---")
def program():
	firstInput = raw_input("")
	counter = 0;
	while(int(counter) < int(firstInput)):
		number = int(raw_input(""))
		ns = []
		es = []
		ns,es = ingenuo(number)	
		gauss(ns,es, number)
		counter += 1
program()