'''
From https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

1. Randomly generate two lists to test this

2. Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common = []

for element in a:
	if element in b and element not in common:
		common.append(element)

if common == []:
	print("The lists do not share any elements.")
else:
	print(common)

#In one line of code
print([common for element in a if element in b and element not in common])

#With randomized lists
import random

r1 = random.randint(1,100)
r2 = random.randint(1,100)
c = []
d = []
e = []

for x in range(r1):
	c.append(random.randint(1,100))

for x in range(r2):
	d.append(random.randint(1,100))

for element in c:
	if element in d and element not in e:
		e.append(element)

'''
#Check randomized lists
c.sort()
d.sort()

print(c)
print(d)
'''

e.sort()

if e == []:
	print("The lists do not share any elements.")
else:
	print(e)