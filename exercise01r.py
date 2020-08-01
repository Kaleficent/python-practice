"""
From https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

1. Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)

2. Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
"""
from datetime import datetime

def vname(name):
    while name.isalpha() == False:
        name = input("Please use only alphabetic characters: ")
    return name

def vnum(num):
    while num.isdigit() == False:
        num = input("Please enter only whole numbers: ")
    num = int(num)
    return num

def repeat(times, birth, year, current):
    for x in range(times):
        print("Thanks, " + name + "!\nYou were born in the year " + str(birth) + ".")
        if year <= current:
            print("You turned 100 in " + str(year) + ".\n")
        else:
            print("You will turn 100 in the year " + str(year) + ".\n")

name = input("Please enter your name: ")
name = vname(name)

age = input("Please enter your age: ")
age = vnum(age)

current = datetime.now().year

cent = 100 - age + current
birth = current - age

repeats = input("How many times would you like to me to repeat my reply? ")
repeats = vnum(repeats)

repeat(repeats, birth, cent, current)