"""
From: https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html

Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
"""
import random
a = [5, 10, 15, 20, 25]
c = [random.randint(1,30) for x in range(20)]

def firstlast(lista):
    return [lista[0], lista[len(lista) - 1]]

b = firstlast(a)
print(b)
print(a)

print("\n")

d = firstlast(c)
print(d)
print(c)