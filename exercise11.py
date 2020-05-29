"""
From: https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you.
"""
import math

# Check that a non-zero natural number has been entered
def valid(number):
    while number.isdigit() == False or int(number) == 0:
        number = input("Please enter a whole non-zero number: ")
    number = int(number)
    return number

# Check primality of a number
def prime(number):
    isprime = []
    root = math.sqrt(number)
    for element in range(2, int(root)):
        # Check for a remainder
        if number % element == 0:
            isprime.append(element)
        # Check for elements in isprime and breaks at first such element
        if len(isprime) != 0:
            print(str(number) + " is not prime.")
            return
    print(str(number) + " is prime.")

num = "a"
num = valid(num)
prime(num)