"""
From https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
"""

test = "!"

while test.isalnum() == False:
	test = input("Enter a word or whole number, and I will tell you if it is a palindrome: ")

test = test.lower()

#Method using string slicing L[start:end:interval]
if test == test[::-1]:
	print("Your string is a palindrome!")
else:
	print("Your string is not a palindrome.")

"""
#Method using for loop and lists

pal = []
lap = []

for c in test:
	pal.append(c)
	lap.append(c)

lap.reverse()

if pal == lap:
	print("Your string is a palindrome!")
else:
	print("Your string is not a palindrome.")
"""