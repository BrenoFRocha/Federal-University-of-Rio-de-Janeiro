def program():
	n = int(raw_input())
	N = []
	CN = []
	j = 3
	while(j <= n):
		N.append(j)
		CN.append(j)
		j += 2
	print(N)
	t = len(N)
	i = 0
	print(int(n**0.5))
	while(2*i+3 <= n ** 0.5):
		j = 2*i+3
		k = (j*j-3)/2
		print(str(j)+" "+str(N[k])+" "+str(k))
		TL = []
		while(k < t):
			TL.append(CN[k])
			N[k] = 0
			k += j
		print(TL)
		L = []
		s = len(N)
		p = 0
		while(p < s):
			if(N[p] != 0):
				L.append(N[p])
			p += 1
		print(L)
		i += 1
		while(N[i] == 0):
			i += 1
	L = [2]
	s = len(N)
	p = 0
	while(p < s):
		if(N[p] != 0):
			L.append(N[p])
		p += 1
	print(L)
program()
