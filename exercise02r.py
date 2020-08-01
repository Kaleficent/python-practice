# Refactor of Exercise 2
num = "a"
check = "b"

# Check that a non-zero natural number has been entered
def valid(number):
	while number.isdigit() == False or int(number) == 0:
		number = input("Please enter a whole non-zero number: ")
	return number

# Check whether a number is divisible by 2 or 4
def checkeven(number):
	if int(number) % 2 == 0:
		print(number + " is even.")
		if int(number) % 4 == 0:
			print (number + " is divisible by 4.")
	else:
		print(number + " is odd.")

# Check if any non-zero natural number is divisible by another
def divisible(number, divisor):
	remainder = int(number) % int(divisor)
	if remainder == 0:
		print(number + " is evenly divisible by " + divisor + ".")
	else:
		print(number + " is not evenly divisible by " + divisor + ".")

num = valid(num)
checkeven(num)

num = "a"
num = valid(num)
check = valid(check)
divisible(num, check)