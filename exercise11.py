"""
From: https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you.
"""

# Check that a non-zero natural number has been entered
def valid(number):
    while number.isdigit() == False or int(number) == 0:
        number = input("Please enter a whole non-zero number: ")
    number = int(number)
    return number

# Check if a number is divisible by any other smaller numbers
def prime(number, divisor):
    isprime = []
    for element in divisor:
        # Check for a remainder
        if number % element == 0:
            isprime.append(element)
        # Check for elements in isprime and breaks at first such element
        if len(isprime) != 0:
            print(str(number) + " is not prime.")
            return number
    print(str(number) + " is prime.")
    return number

num = "a"
num = valid(num)
div = range(2, num)
prime(num, div)