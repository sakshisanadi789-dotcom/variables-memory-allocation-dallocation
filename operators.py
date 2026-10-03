# def calculate(first_number, second_number):
# 	print("Addition:", first_number + second_number)
# 	print("Subtraction:", first_number - second_number)
# 	print("Multiplication:", first_number * second_number)

# 	if second_number == 0:
# 		print("Division: undefined (cannot divide by zero)")
# 		print("Floor division: undefined (cannot divide by zero)")
# 		print("Remainder: undefined (cannot divide by zero)")
# 		return

# 	print("Division:", first_number / second_number)
# 	print("Floor division:", first_number // second_number)
# 	print("Remainder:", first_number % second_number)


# first_number = int(input("Enter the first number: "))
# second_number = int(input("Enter the second number: "))
# calculate(first_number, second_number)


def check_number(number):
	if number % 2 == 0:
		print(number, "is even")
	else:
		print(number, "is odd")

	print("Divisible by 3:", number % 3 == 0)
	print("Divisible by 5:", number % 5 == 0)


def check_marks(marks):
	if marks >= 75:
		return "Distinction"
	if marks >= 35:
		return "Pass"
	return "Fail"


number = int(input("Enter an integer to check: "))
check_number(number)

marks = int(input("Enter the student's marks: "))
print(check_marks(marks))
