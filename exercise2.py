"""
From https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

1. If the number is a multiple of 4, print out a different message.

2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""

number = "x"
while number.isdigit() == False:
	number = input("Please enter a whole number: ")
number = int(number)

remainder = number % 2
multiple = number % 4

if remainder == 0:
	if multiple == 0:
		print(str(number) + " is a multiple of 4.")
	else:
		print(str(number) + " is even.")
else:
	print(str(number) + " is odd.")
	
check = "y"
while check.isdigit() == False:
	check = input("Please enter another whole number. ")
check = int(check)

divisible = number % check

if divisible == 0:
	print(str(number) + " is evenly divisible by " + str(check) + "!")
	result = int(number / check)
	print("The result is " + str(result) + ".")
else:
	print(str(number) + " is not evenly divisible by " + str(check) + ".")