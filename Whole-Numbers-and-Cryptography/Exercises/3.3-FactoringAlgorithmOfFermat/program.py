def program():
	firstInput = raw_input("")
	counter = 0;
	while(int(counter) < int(firstInput)):
		counter += 1
		number = int(raw_input(""))
		x = (int)(number ** 0.5)
		y = 0
		print(str(x) + " " + str(y) + " N")
		while(number != ((x**2) - (y**2))):
			x += 1
			y = (int)(((x**2) - number) ** 0.5) 
			if(number != ((x**2) - (y**2))):
				print(str(x) + " " + str(y) + " N")
			else:
				if(x + y == number and number != ((x**2) - (y**2))):
					print(str(x) + " " + str(y) + " N")
				elif(x + y != number):
					print(str(x) + " " + str(y) + " S")
				print(str(x-y) + " " + str(x+y))
				print("---")
program()

