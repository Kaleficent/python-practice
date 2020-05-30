"""
From: https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html

Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras:

1. Write two different functions to do this - one using a loop and constructing a list, and another using sets.

2. Go back and do Exercise 5 using sets, and write the solution for that in a different function.
"""
import random

# List method
def uniqueloop(lista):
    unique = []
    for element in lista:
	    if element not in unique:
		    unique.append(element)
    unique.sort()
    return unique

# Set method
def uniqueset(lista):
    a = set(lista)
    return list(a)

# Compare two lists
def comparesets(a, b):
    a = set(a)
    b = set(b)
    return [x for x in a if x in b]

a = [random.randint(1,10) for x in range(20)]
b = [random.randint(1,10) for x in range(15)]

print(a)

loopa = uniqueloop(a)
print(loopa)

seta = uniqueset(a)
print(seta)

print("\n")

print(a)
print(b)
compare = comparesets(a, b)
print(compare)