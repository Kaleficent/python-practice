"""
From: https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html

Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""
def valid(number):
    while number.isdigit() == False or int(number) == 0:
        number = input("Please enter a whole non-zero number: ")
    number = int(number)
    return number

def fibonacci(times):
    count = 1
    fib = [1, 1]
    while count + 2 <= times:
        sum = fib[count] + fib[count - 1]
        fib.append(sum)
        count = count + 1
    if times == 1:
        print("[1]")
    else:
        print(fib)

times = input("How many numbers of the Fibonnaci Sequence would you like to display? ")
times = valid(times)

fib = fibonacci(times)