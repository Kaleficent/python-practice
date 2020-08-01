"""
From https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
"""

number = "x"
while number.isdigit() == False:
	number = input("Please enter a number: ")
number = int(number)

divisor = range(2, number)
divisible = []

"""
#test to check logic
for element in divisor:
	if number % element == 0:
		print(str(number) + " is divisible by " + str(element))
	else:	
		print(str(number) + " is not divisible by " + str(element))
"""

#simplified code
for element in divisor:
	if number % element == 0:
		divisible.append(element)

if divisible == []:
	print(str(number) + " is prime.")
else:
	print(divisible)