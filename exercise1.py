"""
From https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

1. Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)

2. Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
"""

name = "!"
while name.isalpha() == False:
	name = input("Please enter your name using only alphabetic characters: ")
	
age = "x"
while age.isdigit() == False:
	age = input("Please enter your age using only whole numbers: ")
age = int(age)

current = "y"
while current.isdigit() == False:
	current = input("Please enter a year (A.D.): ")
current = int(current)

year = 100 - age + current

repeat = "z"
while repeat.isdigit() == False:
	repeat = input("How many times would you like to me to repeat my reply? ")
repeat = int(repeat)

for x in range(repeat):
	if year <= current:
		print("Thanks, " + name + "! You turned 100 in " + str(year) + ".")
	else:
		print("Thanks, " + name + "! You will turn 100 in the year " + str(year) + ".")