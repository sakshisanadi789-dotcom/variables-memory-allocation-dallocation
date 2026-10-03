def calculate(first_number, second_number):
	print("Addition:", first_number + second_number)
	print("Subtraction:", first_number - second_number)
	print("Multiplication:", first_number * second_number)

	if second_number == 0:
		print("Division: undefined (cannot divide by zero)")
		print("Floor division: undefined (cannot divide by zero)")
		print("Remainder: undefined (cannot divide by zero)")
		return

	print("Division:", first_number / second_number)
	print("Floor division:", first_number // second_number)
	print("Remainder:", first_number % second_number)


first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
calculate(first_number, second_number)