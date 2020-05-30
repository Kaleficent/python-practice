"""
Refactor of Exercise 5 using two different types of function
"""
import random

# List method
def compareloop(a, b):
    common = []
    for element in a:
	    if element in b and element not in common:
		    common.append(element)
    common.sort()
    return common

# Set method
def comparesets(a, b):
    a = set(a)
    b = set(b)
    return [x for x in a if x in b]

a = [random.randint(1,10) for x in range(20)]
b = [random.randint(1,10) for x in range(15)]

c = compareloop(a,b)
print(c)

c = comparesets(a, b)
print(c)