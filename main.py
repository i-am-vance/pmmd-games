from random import randrange


def plus():
	digit_one = int(input("Enter the first number :"))
	digit_tow = int(input("Enter the second number :"))

	first_number = randrange(digit_one)
	second_number = randrange(digit_tow)

	print("%s + %s" %(first_number, second_number))
	
	plus_r_number = first_number + second_number

	user_input = int(input("Enter the answer: "))

	if user_input == plus_r_number :
		print("The answer is correct :)")
	else:
		print("The answer is wrong :/")

def minus():
	digit_one = int(input("Enter the first number :"))
	digit_tow = int(input("Enter the second number :"))

	first_number = randrange(digit_one)
	second_number = randrange(digit_tow)
	
	print("%s - %s" %(first_number, second_number))

	minus_r_number = first_number - second_number 

	user_input = int(input("Enter the answer: "))

	if user_input == plus_r_number :
		print("The answer is correct :)")
	else:
		print("The answer is wrong :/")

def multiplication():
	digit_one = int(input("Entrer the first number :"))
	digit_tow = int(input("Entrer the second number :"))

	first_number = randrange(digit_one)
	second_number = randrange(digit_tow)

	print("%s * %s" %(first_number, second_number))

	multiplication_r_number = first_number * second_number

	user_input = int(input("Enter the answer: "))

	if user_input == plus_r_number :
		print("The answer is correct :)")
	else:
		print("The answer is wrong :/")

def division():
	digit_one = int(input("Entrer the first number :"))
	digit_tow = int(input("Entrer the second number :"))

	first_number = randrange(digit_one)
	second_number = randrange(digit_tow)

	print("%s / %s" %(first_number, second_number)) 	
	
	division_r_number = first_number / second_number

	user_input = int(input("Enter the answer: "))

	if user_input == division_r_number :
		print("The answer is correct :)")
	else:
		print("The answer is wrong :/")







