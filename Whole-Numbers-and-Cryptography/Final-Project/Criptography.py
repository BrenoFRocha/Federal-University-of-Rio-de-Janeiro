#Bibliotecas utilizadas
import random
import os.path
from hashlib import sha224
#Demais algoritmos
#0
def MDC(n1,n2):
	number1 = n1
	number2 = n2
	q = 0
	r = 0
	while(number2 != 0):
		r = number1%number2
		q = number1/number2
		number1 = number2
		number2 = r	
	return number1
def ExpModular(b,e,m):
	result = 1
	base = b
	exponent = e
	module = m
	while(exponent != 0):
		if(exponent % 2 == 0):
			exponent /= 2
			base *= base
			base = base%module
		else:
			exponent = (exponent-1)/2
			result= (result*base)%module
			base *= base
			base = base%module
	return result
def MillerRabin(number,base):
	n = number
	b = base
	if(n % 2 == 0 and n != 2):
		return "Composto"
	elif(n == 1 or n == 2 or n == 3):
		return "Primo"
	else:
		k = 0
		q = n - 1
		while(q % 2 == 0):
			k += 1
			q /= 2
		t = ExpModular(b,q,n)
		if(t == 1 or t == n-1):
			return "Primo"
		else:
			i = 1
			while (i < k):
				t = ExpModular(t,2,n)
				if(t == n-1):
					return "Primo"
				else:
					i += 1
			return "Composto"
def EuclidianoEstendido(n1,n2):
	number1 = n1
	number2 = n2
	q = 0
	r = 0
	savedX = 0
	x1 = 1
	x2 = 0
	y1 = 0
	y2 = 1
	while(number2 != 0):
		r = number1 % number2
		q = number1/number2
		number1 = number2
		number2 = r
		temp = y1
		temp -= (y2*q)
		y1 = y2
		y2 = temp 	
		temp = x1
		temp -= (x2*q)
		x1 = x2
		x2 = temp
		if(number2 != 0):
			savedX = x2
	return savedX;
def ConvertToHex(decimal):
    n = (decimal % 16)
    temp = ""
    if (n < 10):
        temp = n
    if (n == 10):
        temp = "A"
    if (n == 11):
        temp = "B"
    if (n == 12):
        temp = "C"
    if (n == 13):
        temp = "D"
    if (n == 14):
        temp = "E"
    if (n == 15):
        temp = "F"
    if (decimal - n != 0):
        return ConvertToHex(decimal / 16) + str(temp)
    else:
        return str(temp)
def ConvertToDec(hexadecimal):
	n = hexadecimal
	result = int(n,16)
	return str(result)
def Module(n,m):
	result = 0
	num = n
	mod = m
	if(num < 0):
		num *= -1
		if(num < mod):
			result = mod - num
		else:
			result = num%mod
	else:
		result = num%mod
	return result
#-----------------------------------------------------------------------------------------------------------------------------
#1
#Metodos para o modo de geracao de chaves
def SaveKeysRSA(n,e,d):
	chose = ''
	while(chose != "Salvar" and chose != "Exibir"):
		print("Deseja 'Salvar' ou 'Exibir' no terminal as chaves e componentes gerados?")
		chose = raw_input()
		if(chose == "Salvar"):
			print("Voce escolheu 'Salvar' as chaves e componentes gerados.")
			print("")
			print("Qual o nome do arquivo onde a chave publica sera guardada?")
			fName = raw_input("")
			publicF = open(fName, 'w')
			publicF.write(n + "\n")
			publicF.write(e + "\n")
			print("")
			print("Qual o nome do arquivo onde a chave privada sera guardada?")
			fName = raw_input("")
			privateF = open(fName, 'w')
			privateF.write(n + "\n")
			privateF.write(d + "\n")
			print("")
			print("Chaves salvas com sucesso!")
		elif(chose == "Exibir"):
			print("Voce escolheu 'Exibir' as chaves e componentes gerados.")
			print("")
			print("Chave Publica:")
			print(n)
			print(e)
			print("")
			print("Chave Privada:")
			print(n)
			print(d)
			print("")
		else:
			print("Entrada invalida, tente novamente.")
			print("")
def SaveKeysElGamal(p,g,c,a):
	chose = ''
	while(chose != "Salvar" and chose != "Exibir"):
		print("Deseja 'Salvar' ou 'Exibir' no terminal as chaves e componentes gerados?")
		chose = raw_input()
		if(chose == "Salvar"):
			print("Voce escolheu 'Salvar' as chaves e componentes gerados.")
			print("")
			print("Qual o nome do arquivo onde a chave publica sera guardada?")
			fName = raw_input("")
			publicF = open(fName, 'w')
			publicF.write(p + "\n")
			publicF.write(g + "\n")
			publicF.write(c + "\n")
			print("")
			print("Qual o nome do arquivo onde a chave privada sera guardada?")
			fName = raw_input("")
			privateF = open(fName, 'w')
			privateF.write(p + "\n")
			privateF.write(g + "\n")
			privateF.write(a + "\n")
			print("")
			print("Chaves salvas com sucesso!")
		elif(chose == "Exibir"):
			print("Voce escolheu 'Exibir' as chaves e componentes gerados.")
			print("")
			print("Parametros Publicos:")
			print(p)
			print(g)
			print("")
			print("Chave Publica:")
			print(c)
			print("")
			print("Chave Privada:")
			print(a)
			print("")
		else:
			print("Entrada invalida, tente novamente.")
			print("")
def GRSA():
	p = 10
	q = 10
	print("Gerando chaves e componentes...")
	while(MillerRabin(p,2) != "Primo"):
		p = random.getrandbits(128)
	while(MillerRabin(q,2) != "Primo"):
		q = random.getrandbits(128)
	n = p*q
	phiN = (p-1)*(q-1)
	e = 2
	while(e < phiN and MDC(e,phiN) != 1):
		e += 1
	d = EuclidianoEstendido(e,phiN)
	if(d < 0):
		d = Module(d,phiN)
	else:
		d = d%phiN
	e = ConvertToHex(e)
	d = ConvertToHex(d)
	n = ConvertToHex(n)
	while(len(e) < 64):
		e = "0"+e
	while(len(d) < 64):
		d = "0"+d
	while(len(n) < 64):
		n = "0"+n
	print("Chaves e componentes gerados com sucesso!")
	print("")
	SaveKeysRSA(n,e,d)
def GElGamal():
	q = 10
	p = 10
	g = 2
	a = 0
	c = 0
	print("Gerando chaves e componentes...")
	while(MillerRabin(q,2) != "Primo" or MillerRabin(p,2) != "Primo" or q.bit_length() != 255 or p.bit_length() != 256):
		q = random.getrandbits(255)
		p = q*2+1
	while(ExpModular(g, q, p) == 1):
		g += 1
	a = random.randint(2,p-2)
	c = ExpModular(g, a, p)
	p = ConvertToHex(p)
	g = ConvertToHex(g)
	c = ConvertToHex(c)
	a = ConvertToHex(a)
	while(len(p) < 64):
		p = "0"+p
	while(len(g) < 64):
		g = "0"+g
	while(len(c) < 64):
		c = "0"+c
	while(len(a) < 64):
		a = "0"+a
	print("Chaves e componentes gerados com sucesso!")
	print("")
	SaveKeysElGamal(p,g,c,a)
def GCriptografia():
	chose = ''
	while(chose != "RSA" and chose != "El Gamal"):
		print("Voce deseja gerar chaves para 'RSA' ou para 'El Gamal'?")
		chose = raw_input()
		if(chose == "RSA"):
			print("Voce escolheu gerar chaves para RSA.")
			print("")
			GRSA()
		elif(chose == "El Gamal"):
			print("Voce escolheu gerar chaves para El Gamal.")
			print("")
			GElGamal()
		else:
			print("Entrada invalida, tente novamente.")
			print("")	
#Programa principal de geracao de chaves
def Gprogram():
	chose = ''
	while(chose != "Assinatura Digital" and chose != "Criptografia"):
		print("Voce deseja gerar chaves de 'Assinatura Digital' ou chaves de 'Criptografia'?")
		chose = raw_input()
		if(chose == "Criptografia"):
			print("Voce escolheu gerar chaves de Criptografia.")
			print("")
			GCriptografia()
		elif(chose == "Assinatura Digital"):
			print("Voce escolheu gerar chaves de Assinatura Digital.")
			print("")
			GElGamal()
		else:
			print("Entrada invalida, tente novamente.")
			print("")
#-----------------------------------------------------------------------------------------------------------------------------
#2
#Metodos para o modo de encriptacao (pura)
def ERSA(fName):
	chose = ''
	n = 0
	e = 0
	while(chose != "Digitar" and chose != "Leia"):
		print("Voce deseja 'Digitar' ou deseja que o programa 'Leia' a chave publica de um arquivo?")
		chose = raw_input()
		if(chose == "Digitar"):
			print("Voce escolheu digitar a chave publica do RSA.")
			print("")
			n = raw_input()
			e = raw_input()
			print("")
		elif(chose == "Leia"):
			print("Voce escolheu ler a chave publica do RSA de um arquivo.")
			print("")
			fileOK = False
			chosef = ''
			while(fileOK == False):
				print("Qual o nome do arquivo que contem a chave publica para encriptar?")
				chosef = raw_input()
				if(os.path.exists(chosef)):
					print("Arquivo encontrado!")
					print("")
					fileOK = True
					publicF = open(chosef, 'r')
					n = publicF.readline()
					e = publicF.readline()
					n = n[:-1]
					e = e[:-1]
				else:
					print("Arquivo nao existe, tente novamente.")
					print("")
		else:
			print("Entrada invalida, tente novamente.")
			print("")
	primaryF = open(fName,'r')
	content = primaryF.read()
	c = 0
	print("Escolha o nome do arquivo quando encriptado:")
	nameF = raw_input()
	newF = open(nameF, 'w')
	block = ''
	print("")
	print("Encriptando...")
	while(c < len(content)):
		block = (ord(content[c])+100)
		block = ExpModular(block, int(ConvertToDec(e)), int(ConvertToDec(n)))
		newF.write(str(block)+"\n")
		c += 1
	print("Arquivo encriptado com sucesso!")
def EElGamal(fName):
	chose = ''
	p = 0
	g = 0
	c = 0
	while(chose != "Digitar" and chose != "Leia"):
		print("Voce deseja 'Digitar' ou deseja que o programa 'Leia' a chave publica de um arquivo?")
		chose = raw_input()
		if(chose == "Digitar"):
			print("Voce escolheu digitar a chave publica do El Gamal.")
			print("")
			p = raw_input()
			g = raw_input()
			c = raw_input()
			print("")
		elif(chose == "Leia"):
			print("Voce escolheu ler a chave publica do El Gamal de um arquivo.")
			print("")
			fileOK = False
			chosef = ''
			while(fileOK == False):
				print("Qual o nome do arquivo que contem a chave publica para encriptar?")
				chosef = raw_input()
				if(os.path.exists(chosef)):
					print("Arquivo encontrado!")
					print("")
					fileOK = True
					publicF = open(chosef, 'r')
					p = publicF.readline()
					g = publicF.readline()
					c = publicF.readline()
					p = p[:-1]
					g = g[:-1]
					c = c[:-1]
				else:
					print("Arquivo nao existe, tente novamente.")
					print("")
		else:
			print("Entrada invalida, tente novamente.")
			print("")
	primaryF = open(fName,'r')
	content = primaryF.read()
	l = 0
	print("Escolha o nome do arquivo quando encriptado:")
	nameF = raw_input()
	newF = open(nameF, 'w')
	block = ''
	print("")
	print("Encriptando...")
	p = int(ConvertToDec(p))
	g = int(ConvertToDec(g))
	c = int(ConvertToDec(c))
	while(l < len(content)):
		block = (ord(content[l])+100)
		k = random.randint(2,p-2)
		s = ExpModular(g, k, p)
		t = (block*ExpModular(c, k, p))%p
		newF.write(str(s)+"\n")
		newF.write(str(t)+"\n")
		l += 1
	print("Arquivo encriptado com sucesso!")
#Programa principal de encriptacao
def Eprogram():
	chose = ''
	chosef = ''
	fileOK = False
	while(chose != "RSA" and chose != "El Gamal"):
		print("Voce deseja encriptar com 'RSA' ou com 'El Gamal'?")
		chose = raw_input()
		if(chose == "RSA"):
			print("Voce escolheu encriptar com RSA.")
			print("")
		elif(chose == "El Gamal"):
			print("Voce escolheu encriptar com El Gamal.")
			print("")
		else:
			print("Entrada invalida, tente novamente.")
			print("")
	while(fileOK == False):
		print("Qual o nome do arquivo que voce deseja encriptar?")
		chosef = raw_input()
		if(os.path.exists(chosef)):
			print("Arquivo encontrado!")
			print("")
			fileOK = True
			if(chose == "RSA"):
				ERSA(chosef)
			else:
				EElGamal(chosef)
		else:
			print("Arquivo nao existe, tente novamente.")
			print("")
#-----------------------------------------------------------------------------------------------------------------------------
#3
#Metodos para o modo de decriptacao (pura)
def DRSA(fName):
	chose = ''
	n = 0
	d = 0
	while(chose != "Digitar" and chose != "Leia"):
		print("Voce deseja 'Digitar' ou deseja que o programa 'Leia' a chave privada de um arquivo?")
		chose = raw_input()
		if(chose == "Digitar"):
			print("Voce escolheu digitar a chave privada do RSA.")
			print("")
			n = raw_input()
			d = raw_input()
			print("")
		elif(chose == "Leia"):
			print("Voce escolheu ler a chave privada do RSA de um arquivo.")
			print("")
			fileOK = False
			chosef = ''
			while(fileOK == False):
				print("Qual o nome do arquivo que contem a chave privada para decriptar?")
				chosef = raw_input()
				if(os.path.exists(chosef)):
					print("Arquivo encontrado!")
					print("")
					fileOK = True
					privateF = open(chosef, 'r')
					n = privateF.readline()
					d = privateF.readline()
					n = n[:-1]
					d = d[:-1]
				else:
					print("Arquivo nao existe, tente novamente.")
					print("")
		else:
			print("Entrada invalida, tente novamente.")
			print("")
	primaryF = open(fName,'r')
	print("Escolha o nome do arquivo quando decriptado:")
	nameF = raw_input()
	newF = open(nameF, 'w')
	line = primaryF.readline()
	print("")
	print("Decriptografando...")
	while(line != ''):
		block = line
		block = ExpModular(int(block), int(ConvertToDec(d)), int(ConvertToDec(n)))
		block = chr((int(block)-100))
		newF.write(block)
		line = primaryF.readline()
	print("Arquivo decriptografado com sucesso!")
def DElGamal(fName):
	chose = ''
	p = 0
	g = 0
	a = 0
	while(chose != "Digitar" and chose != "Leia"):
		print("Voce deseja 'Digitar' ou deseja que o programa 'Leia' a chave privada de um arquivo?")
		chose = raw_input()
		if(chose == "Digitar"):
			print("Voce escolheu digitar a chave privada do El Gamal.")
			print("")
			p = raw_input()
			g = raw_input()
			a = raw_input()
			print("")
		elif(chose == "Leia"):
			print("Voce escolheu ler a chave privada do El Gamal de um arquivo.")
			print("")
			fileOK = False
			chosef = ''
			while(fileOK == False):
				print("Qual o nome do arquivo que contem a chave privada para decriptar?")
				chosef = raw_input()
				if(os.path.exists(chosef)):
					print("Arquivo encontrado!")
					print("")
					fileOK = True
					privateF = open(chosef, 'r')
					p = privateF.readline()
					g = privateF.readline()
					a = privateF.readline()
					p = p[:-1]
					g = g[:-1]
					a = a[:-1]
				else:
					print("Arquivo nao existe, tente novamente.")
					print("")
		else:
			print("Entrada invalida, tente novamente.")
			print("")
	p = int(ConvertToDec(p))
	g = int(ConvertToDec(g))
	a = int(ConvertToDec(a))
	primaryF = open(fName,'r')
	print("Escolha o nome do arquivo quando decriptado:")
	nameF = raw_input()
	newF = open(nameF, 'w')
	blockS = primaryF.readline()
	blockT = primaryF.readline()
	print("")
	print("Decriptografando...")
	while(blockS != ''):
		tempS = ExpModular(int(blockS), (p-1-a), p)
		block = ((tempS*int(blockT))%p)
		block = chr((int(block)-100))
		newF.write(block)
		blockS = primaryF.readline()
		blockT = primaryF.readline()
	print("Arquivo decriptografado com sucesso!")
def Dprogram():
	chose = ''
	chosef = ''
	fileOK = False
	while(chose != "RSA" and chose != "El Gamal"):
		print("Voce deseja decriptar com 'RSA' ou com 'El Gamal'?")
		chose = raw_input()
		if(chose == "RSA"):
			print("Voce escolheu decriptar com RSA.")
			print("")
		elif(chose == "El Gamal"):
			print("Voce escolheu decriptar com El Gamal.")
			print("")
		else:
			print("Entrada invalida, tente novamente.")
			print("")
	while(fileOK == False):
		print("Qual o nome do arquivo que voce deseja decriptar?")
		chosef = raw_input()
		if(os.path.exists(chosef)):
			print("Arquivo encontrado!")
			print("")
			fileOK = True
			if(chose == "RSA"):
				DRSA(chosef)
			else:
				DElGamal(chosef)
		else:
			print("Arquivo nao existe, tente novamente.")
			print("")

#-----------------------------------------------------------------------------------------------------------------------------
#4
#Metodos para o modo de assinatura digital (pura)
def ADigital(primaryF, prime, generator, privateK):
	fileAD = open(primaryF, 'r')
	content = fileAD.read()
	charRead = 0
	allFText = ''
	print("Lendo arquivo...")
	while(charRead < len(content)):
		block = (ord(content[charRead]))
		ConvertToBin = lambda x: format(x, 'b')
		block = ConvertToBin(block)
		allFText = str(allFText) + str(block)
		charRead += 1
	print("Arquivo lido!")
	print("")
	p = int(ConvertToDec(prime))
	g = int(ConvertToDec(generator))
	a = int(ConvertToDec(privateK))
	k = random.randint(2,p-2)
	while(MDC(k, p-1) != 1):
		k = random.randint(2,p-2)
	r = ExpModular(g, k, p)
	kL = EuclidianoEstendido(k, p-1)
	ConvertToBin = lambda x: format(x, 'b')
	h = sha224(allFText).hexdigest()
	h = int(ConvertToDec(h))
	h = int(ConvertToBin(h))
	s = (kL*(h-a*r))%(p-1)
	r = int(r)
	s = int(s)
	r = ConvertToHex(r)
	s = ConvertToHex(s)
	while(len(r) < 64):
		r = "0"+r
	while(len(s) < 64):
		s = "0"+s
	print("Qual o nome do arquivo onde deseja salvar sua assinatura?")
	fName = raw_input("")
	fileF = open(fName, 'w')
	fileF.write(r +"\n")
	fileF.write(s +"\n")
	print("Arquivo assinado com sucesso!")
def ADprogram():
	p = 10
	g = 10
	a = 10
	chose = ''
	chosef1 = ''
	chosef2 = ''
	file1OK = False
	while(file1OK == False):
		print("Qual o nome do arquivo que voce deseja assinar?")
		chosef1 = raw_input()
		if(os.path.exists(chosef1)):
			print("Arquivo encontrado!")
			print("")
			file1OK = True
		else:
			print("Arquivo nao existe, tente novamente.")
			print("")
	while(chose != "Digitar" and chose != "Leia"):
		print("Voce deseja 'Digitar' ou deseja que o programa 'Leia' a chave privada de assinatura digital?")
		chose = raw_input()
		if(chose == "Digitar"):
			print("Voce escolheu digitar a chave privada de Assinatura Digital.")
			print("")
			p = raw_input()
			g = raw_input()
			a = raw_input()
			print("")
		elif(chose == "Leia"):
			print("Voce escolheu ler a chave privada de Assinatura Digital de um arquivo.")
			print("")
			file2OK = False
			while(file2OK == False):
				print("Qual o nome do arquivo que contem a chave privada para assinar?")
				chosef2 = raw_input()
				if(os.path.exists(chosef2)):
					print("Arquivo encontrado!")
					print("")
					file2OK = True
					privateF = open(chosef2, 'r')
					p = privateF.readline()
					g = privateF.readline()
					a = privateF.readline()
					p = p[:-1]
					g = g[:-1]
					a = a[:-1]
				else:
					print("Arquivo nao existe, tente novamente.")
					print("")
		else:
			print("Entrada invalida, tente novamente.")
			print("")
	ADigital(chosef1, p, g, a)
#-----------------------------------------------------------------------------------------------------------------------------
#5
#Metodos para o modo de verificacao assinatura digital (pura)
def VADigital(f1, f2, prime, generator, public):
	fileAD = open(f2, 'r')
	p = int(ConvertToDec(prime))
	g = int(ConvertToDec(generator))
	r = fileAD.readline()
	s = fileAD.readline()
	r = r[:-1]
	s = s[:-1]
	r = int(ConvertToDec(r))
	s = int(ConvertToDec(s))
	v = int(ConvertToDec(public))

	if(r < 1 or r > p-1):
		print("Assinatura Invalida")
	else:
		fileP = open(f1, 'r')
		content = fileP.read()
		charRead = 0
		allFText = ''
		print("Lendo arquivo...")
		while(charRead < len(content)):
			block = (ord(content[charRead]))
			ConvertToBin = lambda x: format(x, 'b')
			block = ConvertToBin(block)
			allFText = str(allFText) + str(block)
			charRead += 1
		print("Arquivo lido!")
		print("")
		ConvertToBin = lambda x: format(x, 'b')
		h = sha224(allFText).hexdigest()
		h = int(ConvertToDec(h))
		h = int(ConvertToBin(h))
		u1 = (ExpModular(v, r, p) * ExpModular(r, s, p))%p
		u2 = ExpModular(g, h, p)
		if(u1 == u2):
			print("Assinatura Valida")
		else:
			print("Assinatura Invalida")
def VADprogram():
	file1 = ''
	file2 = ''
	f = False
	p = 0
	g = 0
	v = 0
	while(f == False):
		print("Qual o nome do arquivo que foi assinado digitalmente?")
		file1 = raw_input()
		if(os.path.exists(file1)):
			print("Arquivo encontrado!")
			print("")
			f = True
		else:
			print("Arquivo nao existe, tente novamente.")
			print("")
	f = False
	while(f == False):
		print("Qual o nome da assinatura digital do arquivo?")
		file2 = raw_input()
		if(os.path.exists(file2)):
			print("Arquivo encontrado!")
			print("")
			f = True
		else:
			print("Arquivo nao existe, tente novamente.")
			print("")
	chose = ''	
	while(chose != "Digitar" and chose != "Leia"):
		print("Voce deseja 'Digitar' ou deseja que o programa 'Leia' a chave publica de assinatura digital?")
		chose = raw_input()
		if(chose == "Digitar"):
			print("Voce escolheu digitar a chave privada de Assinatura Digital.")
			print("")
			p = raw_input()
			g = raw_input()
			v = raw_input()
		elif(chose == "Leia"):
			print("Voce escolheu ler a chave privada de Assinatura Digital de um arquivo.")
			print("")
			f = False
			while(f == False):
				print("Qual o nome do arquivo que contem a chave publica de assinatura?")
				chosef = raw_input()
				if(os.path.exists(chosef)):
					print("Arquivo encontrado!")
					print("")
					f = True
					publicF = open(chosef, 'r')
					p = publicF.readline()
					g = publicF.readline()
					v = publicF.readline()
					p = p[:-1]
					g = g[:-1]
					v = v[:-1]
				else:
					print("Arquivo nao existe, tente novamente.")
					print("")
		else:
			print("Entrada invalida, tente novamente.")
			print("")
	VADigital(file1, file2, p, g, v)
#-----------------------------------------------------------------------------------------------------------------------------
#6
#Metodos para o modo de assinatura digital e encriptacao
def AEERSA(s,f):
	oFile = f
	signature = s
	chose = ''
	n = 0
	e = 0
	while(chose != "Digitar" and chose != "Leia"):
		print("Voce deseja 'Digitar' ou deseja que o programa 'Leia' a chave publica de encriptacao de um arquivo?")
		chose = raw_input()
		if(chose == "Digitar"):
			print("Voce escolheu digitar a chave publica do RSA.")
			print("")
			n = raw_input()
			e = raw_input()
			print("")
		elif(chose == "Leia"):
			print("Voce escolheu ler a chave publica do RSA de um arquivo.")
			print("")
			fileOK = False
			chosef = ''
			while(fileOK == False):
				print("Qual o nome do arquivo que contem a chave publica para encriptar?")
				chosef = raw_input()
				if(os.path.exists(chosef)):
					print("Arquivo encontrado!")
					print("")
					fileOK = True
					publicF = open(chosef, 'r')
					n = publicF.readline()
					e = publicF.readline()
					n = n[:-1]
					e = e[:-1]
				else:
					print("Arquivo nao existe, tente novamente.")
					print("")
		else:
			print("Entrada invalida, tente novamente.")
			print("")
	primaryF = open(oFile,'r')
	content = primaryF.read()
	content = content + signature
	c = 0
	print("Escolha o nome do arquivo quando encriptado:")
	nameF = raw_input()
	newF = open(nameF, 'w')
	block = ''
	print("")
	print("Encriptando...")
	while(c < len(content)):
		block = (ord(content[c])+100)
		block = ExpModular(block, int(ConvertToDec(e)), int(ConvertToDec(n)))
		newF.write(str(block)+"\n")
		c += 1
	print("Arquivo encriptado com sucesso!")
def AEEElGamal(s, f):
	oFile = f
	signature = s
	chose = ''
	p = 0
	g = 0
	c = 0
	while(chose != "Digitar" and chose != "Leia"):
		print("Voce deseja 'Digitar' ou deseja que o programa 'Leia' a chave publica de um arquivo?")
		chose = raw_input()
		if(chose == "Digitar"):
			print("Voce escolheu digitar a chave publica do El Gamal.")
			print("")
			p = raw_input()
			g = raw_input()
			c = raw_input()
			print("")
		elif(chose == "Leia"):
			print("Voce escolheu ler a chave publica do El Gamal de um arquivo.")
			print("")
			fileOK = False
			chosef = ''
			while(fileOK == False):
				print("Qual o nome do arquivo que contem a chave publica para encriptar?")
				chosef = raw_input()
				if(os.path.exists(chosef)):
					print("Arquivo encontrado!")
					print("")
					fileOK = True
					publicF = open(chosef, 'r')
					p = publicF.readline()
					g = publicF.readline()
					c = publicF.readline()
					p = p[:-1]
					g = g[:-1]
					c = c[:-1]
				else:
					print("Arquivo nao existe, tente novamente.")
					print("")
		else:
			print("Entrada invalida, tente novamente.")
			print("")
	primaryF = open(oFile,'r')
	content = primaryF.read()
	content = content+signature
	l = 0
	print("Escolha o nome do arquivo quando encriptado:")
	nameF = raw_input()
	newF = open(nameF, 'w')
	block = ''
	print("")
	print("Encriptando...")
	p = int(ConvertToDec(p))
	g = int(ConvertToDec(g))
	c = int(ConvertToDec(c))
	while(l < len(content)):
		block = (ord(content[l])+100)
		k = random.randint(2,p-2)
		s = ExpModular(g, k, p)
		t = (block*ExpModular(c, k, p))%p
		newF.write(str(s)+"\n")
		newF.write(str(t)+"\n")
		l += 1
	print("Arquivo encriptado com sucesso!")
def AEADigital(fileN, prime, generator, privateK):
	fileAD = open(fileN, 'r')
	content = fileAD.read()
	charRead = 0
	allFText = ''
	print("Lendo arquivo...")
	while(charRead < len(content)):
		block = (ord(content[charRead]))
		ConvertToBin = lambda x: format(x, 'b')
		block = ConvertToBin(block)
		allFText = str(allFText) + str(block)
		charRead += 1
	print("Arquivo lido!")
	print("")
	p = int(ConvertToDec(prime))
	g = int(ConvertToDec(generator))
	a = int(ConvertToDec(privateK))
	k = random.randint(2,p-2)
	while(MDC(k, p-1) != 1):
		k = random.randint(2,p-2)
	r = ExpModular(g, k, p)
	kL = EuclidianoEstendido(k, p-1)
	ConvertToBin = lambda x: format(x, 'b')
	h = sha224(allFText).hexdigest()
	h = int(ConvertToDec(h))
	h = int(ConvertToBin(h))
	s = (kL*(h-a*r))%(p-1)
	r = int(r)
	s = int(s)
	r = ConvertToHex(r)
	s = ConvertToHex(s)
	while(len(r) < 64):
		r = "0"+r
	while(len(s) < 64):
		s = "0"+s
	signature = r+s
	print("Arquivo assinado com sucesso!")
	print("")
	return signature
def AEprogram():
	signature = ''
	oFile = ''
	oFileV = False
	p = 0
	g = 0
	a = 0
	while(oFileV == False):
		print("Qual o nome do arquivo que voce deseja encriptar e assinar?")
		oFile = raw_input()
		if(os.path.exists(oFile)):
			print("Arquivo encontrado!")
			print("")
			oFileV = True
		else:
			print("Arquivo nao existe, tente novamente.")
			print("")
	chose = ''
	while(chose != "Digitar" and chose != "Leia"):
		print("Voce deseja 'Digitar' ou deseja que o programa 'Leia' a chave privada de assinatura de um arquivo?")
		chose = raw_input()
		if(chose == "Digitar"):
			print("Voce escolheu digitar a chave privada de assinatura.")
			print("")
			p = raw_input()
			g = raw_input()
			a = raw_input()
			print("")
		elif(chose == "Leia"):
			print("Voce escolheu ler a chave privada de assinatura de um arquivo.")
			print("")
			fileOK = False
			chosef = ''
			while(fileOK == False):
				print("Qual o nome do arquivo que contem a chave privada para a assinatura digital?")
				chosef = raw_input()
				if(os.path.exists(chosef)):
					print("Arquivo encontrado!")
					print("")
					fileOK = True
					privateF = open(chosef, 'r')
					p = privateF.readline()
					g = privateF.readline()
					a = privateF.readline()
					p = p[:-1]
					g = g[:-1]
					a = a[:-1]
				else:
					print("Arquivo nao existe, tente novamente.")
					print("")
		else:
			print("Entrada invalida, tente novamente.")
			print("")
	signature = AEADigital(oFile, p, g, a)
	chosek = ''
	while(chosek != "RSA" and chosek != "El Gamal"):
		print("Voce deseja encriptar com 'RSA' ou com 'El Gamal'?")
		chosek = raw_input()
		if(chosek == "RSA"):
			print("Voce escolheu encriptar com RSA.")
			print("")
			AEERSA(signature, oFile)
		elif(chosek == "El Gamal"):
			print("Voce escolheu encriptar com El Gamal.")
			print("")
			AEEElGamal(signature, oFile)
		else:
			print("Entrada invalida, tente novamente.")
			print("")
#-----------------------------------------------------------------------------------------------------------------------------
#7
#Metodos para o modo de verificacao de assinatura digital e decriptacao
def VDRSA(fName):
	chose = ''
	n = 0
	d = 0
	while(chose != "Digitar" and chose != "Leia"):
		print("Voce deseja 'Digitar' ou deseja que o programa 'Leia' a chave privada de um arquivo?")
		chose = raw_input()
		if(chose == "Digitar"):
			print("Voce escolheu digitar a chave privada do RSA.")
			print("")
			n = raw_input()
			d = raw_input()
		elif(chose == "Leia"):
			print("Voce escolheu ler a chave privada do RSA de um arquivo.")
			print("")
			fileOK = False
			chosef = ''
			while(fileOK == False):
				print("Qual o nome do arquivo que contem a chave privada para decriptar?")
				chosef = raw_input()
				if(os.path.exists(chosef)):
					print("Arquivo encontrado!")
					print("")
					fileOK = True
					privateF = open(chosef, 'r')
					n = privateF.readline()
					d = privateF.readline()
					n = n[:-1]
					d = d[:-1]
				else:
					print("Arquivo nao existe, tente novamente.")
					print("")
		else:
			print("Entrada invalida, tente novamente.")
			print("")
	primaryF = open(fName,'r')
	print("Escolha o nome do arquivo quando decriptado:")
	nameF = raw_input()
	line = primaryF.readline()
	print("")
	print("Decriptografando...")
	temp = ''
	while(line != ''):
		block = line
		block = ExpModular(int(block), int(ConvertToDec(d)), int(ConvertToDec(n)))
		block = chr((int(block)-100))
		temp = temp + block
		line = primaryF.readline()
	print("Arquivo decriptografado com sucesso!")
	z = len(temp)
	r = ''
	s = ''
	while(z > len(temp) - 64):
		z -= 1
		s = temp[z] + s 
	z = len(temp)-64
	while(z > len(temp) - 128):
		z -= 1
		r = temp[z] + r 
	temp = temp[:-128]
	print("")
	return r, s, temp, nameF
def VDElGamal(fName):
	chose = ''
	p = 0
	g = 0
	a = 0
	while(chose != "Digitar" and chose != "Leia"):
		print("Voce deseja 'Digitar' ou deseja que o programa 'Leia' a chave privada de um arquivo?")
		chose = raw_input()
		if(chose == "Digitar"):
			print("Voce escolheu digitar a chave privada do El Gamal.")
			print("")
			p = raw_input()
			g = raw_input()
			a = raw_input()
		elif(chose == "Leia"):
			print("Voce escolheu ler a chave privada do El Gamal de um arquivo.")
			print("")
			fileOK = False
			chosef = ''
			while(fileOK == False):
				print("Qual o nome do arquivo que contem a chave privada para decriptar?")
				chosef = raw_input()
				if(os.path.exists(chosef)):
					print("Arquivo encontrado!")
					print("")
					fileOK = True
					privateF = open(chosef, 'r')
					p = privateF.readline()
					g = privateF.readline()
					a = privateF.readline()
					p = p[:-1]
					g = g[:-1]
					a = a[:-1]
				else:
					print("Arquivo nao existe, tente novamente.")
					print("")
		else:
			print("Entrada invalida, tente novamente.")
			print("")
	p = int(ConvertToDec(p))
	g = int(ConvertToDec(g))
	a = int(ConvertToDec(a))
	primaryF = open(fName,'r')
	print("Escolha o nome do arquivo quando decriptado:")
	nameF = raw_input()
	temp = ''
	blockS = primaryF.readline()
	blockT = primaryF.readline()
	print("")
	print("Decriptografando...")
	while(blockS != ''):
		tempS = ExpModular(int(blockS), (p-1-a), p)
		block = ((tempS*int(blockT))%p)
		block = chr((int(block)-100))
		temp = temp + block
		blockS = primaryF.readline()
		blockT = primaryF.readline()
	print("Arquivo decriptografado com sucesso!")
	print("")
	z = len(temp)
	r = ''
	s = ''
	while(z > len(temp) - 64):
		z -= 1
		s = temp[z] + s 
	z = len(temp)-64
	while(z > len(temp) - 128):
		z -= 1
		r = temp[z] + r 
	temp = temp[:-128]
	print("")
	return r,s,temp,nameF
def VADE(ct,rl,sl, prime, generator, public):
	s = sl
	r = rl
	p = int(ConvertToDec(prime))
	g = int(ConvertToDec(generator))
	r = int(ConvertToDec(r))
	s = int(ConvertToDec(s))
	v = int(ConvertToDec(public))
	if(r < 1 or r > p-1):
		print("Assinatura Invalida")
	else:
		content = ct
		charRead = 0
		allFText = ''
		print("Lendo arquivo...")
		while(charRead < len(content)):
			block = (ord(content[charRead]))
			ConvertToBin = lambda x: format(x, 'b')
			block = ConvertToBin(block)
			allFText = str(allFText) + str(block)
			charRead += 1
		print("Arquivo lido!")
		print("")
		ConvertToBin = lambda x: format(x, 'b')
		h = sha224(allFText).hexdigest()
		h = int(ConvertToDec(h))
		h = int(ConvertToBin(h))
		u1 = (ExpModular(v, r, p) * ExpModular(r, s, p))%p
		u2 = ExpModular(g, h, p)
		if(u1 == u2):
			print("Assinatura Valida")
		else:
			print("Assinatura Invalida")
def VDprogram():
	oFile = ''
	oFileV = False
	nFName = ''
	while(oFileV == False):
		print("Qual o nome do arquivo que voce deseja decriptar e verificar assinatura?")
		oFile = raw_input()
		if(os.path.exists(oFile)):
			print("Arquivo encontrado!")
			print("")
			oFileV = True
		else:
			print("Arquivo nao existe, tente novamente.")
			print("")
	chosek = ''
	contF = ''
	r = ''
	s = ''
	while(chosek != "RSA" and chosek != "El Gamal"):
		print("Voce deseja decriptar com 'RSA' ou com 'El Gamal'?")
		chosek = raw_input()
		if(chosek == "RSA"):
			print("Voce escolheu decriptar com 'RSA'.")
			print("")
			r, s, contF, nFName = VDRSA(oFile)
		elif(chosek == "El Gamal"):
			print("Voce escolheu decriptar com 'El Gamal'.")
			print("")
			r, s, contF, nFName = VDElGamal(oFile)
		else:
			print("Entrada invalida, tente novamente.")
			print("")
	chose = ''	
	fFile = open(nFName,'w')
	fFile.write(contF)
	while(chose != "Digitar" and chose != "Leia"):
		print("Voce deseja 'Digitar' ou deseja que o programa 'Leia' a chave publica de assinatura digital?")
		chose = raw_input()
		if(chose == "Digitar"):
			print("Voce escolheu digitar a chave privada de Assinatura Digital.")
			print("")
			p = raw_input()
			g = raw_input()
			v = raw_input()
		elif(chose == "Leia"):
			print("Voce escolheu ler a chave privada de Assinatura Digital de um arquivo.")
			print("")
			f = False
			while(f == False):
				print("Qual o nome do arquivo que contem a chave publica de assinatura?")
				chosef = raw_input()
				if(os.path.exists(chosef)):
					print("Arquivo encontrado!")
					print("")
					f = True
					publicF = open(chosef, 'r')
					p = publicF.readline()
					g = publicF.readline()
					v = publicF.readline()
					p = p[:-1]
					g = g[:-1]
					v = v[:-1]
				else:
					print("Arquivo nao existe, tente novamente.")
					print("")
		else:
			print("Entrada invalida, tente novamente.")
			print("")
	print("Qual o nome do arquivo onde deseja salvar sua assinatura?")
	aName = raw_input("")
	fAD = open(aName, 'w')
	fAD.write(r +"\n")
	fAD.write(s +"\n")
	VADE(contF, r, s, p, g, v)
	
#-----------------------------------------------------------------------------------------------------------------------------
#PROGRAMA PRINCIPAL
def program():
	chose = ""
	print("Bem vindo ao trabalho de final do primeiro semestre de 2017 da disciplina de Numeros Inteiros e Criptografia da Universidade Federal do Rio de Janeiro.")
	print("")
	while(chose != '1' and chose != '2' and chose != '3' and chose != '4' and chose != '5' and chose != '6' and chose != '7'):
		print("Escolha um dos modos abaixo para comecar a utilizar o programa:")
		print("1 - Modo de geracao de chaves.")
		print("2 - Modo de encriptacao (pura).")
		print("3 - Modo de decriptacao (pura).")
		print("4 - Modo de assinatura digital (pura).")
		print("5 - Modo de verificacao de assinatura (pura).")
		print("6 - Modo de assinatura digital e encriptacao (combinados).")
		print("7 - Modo de decriptacao e verificacao de assinatura (combinados).")
		chose = raw_input()
		if(chose == '1'):
			print("Modo de geracao de chaves escolhido.")
			print("")
			Gprogram()
		elif(chose == '2'):
			print("Modo de encriptacao (pura) escolhido.")
			print("")
			Eprogram()
		elif(chose == '3'):
			print("Modo de decriptacao (pura) escolhido.")
			print("")
			Dprogram()
		elif(chose == '4'):
			print("Modo de assinatura digital (pura) escolhido.")
			print("")
			ADprogram()
		elif(chose == '5'):
			print("Modo de verificacao de assinatura (pura) escolhido.")
			print("")
			VADprogram()
		elif(chose == '6'):
			print("Modo de assinatura digital e encriptacao (combinados) escolhido.")
			print("")
			AEprogram()
		elif(chose == '7'):
			print("Modo de decriptacao e verificacao de assinatura (combinados) escolhido.")
			print("")
			VDprogram()
		else:
			print("Entrada invalida, tente novamente.")	
			print("")		
program()