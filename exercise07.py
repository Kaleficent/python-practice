"""
From https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html 
Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
""" 
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#Print a list of only even
print(a[1::2])

#Create new list of only even
b = a[1::2]
print(b)

b.clear()

#General case
b = [x for x in a if x % 2 == 0]
print(b)

b.clear()

#With loop
for x in a:
	if x % 2 == 0:
		b.append(x) 
print(b)
