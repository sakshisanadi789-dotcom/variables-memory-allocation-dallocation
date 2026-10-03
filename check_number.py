def check_number(number):
	if number % 2 == 0:
		print(number, "is even")
	else:
		print(number, "is odd")

	if number % 3 == 0:
		print(number, "is divisible by 3")
	else:
		print(number, "is not divisible by 3")
``
	if number % 5 == 0:
		print(number, "is divisible by 5")
	else:
		print(number, "is not divisible by 5")


number = int(input("Enter an integer: "))
check_number(number)