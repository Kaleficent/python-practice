"""
From https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

1. Keep the game going until the user types “exit”

2. Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""
import random

num = str(random.randint(1, 9))
guess = "x"
count = 0
corr = 0

#Validate input
def valid(guess):
	while guess != "exit":	
		if not(guess.isdigit()):
			guess = guess.lower()
			if guess == "exit":
				return guess
			else:
				guess = input("Enter a number 1-9, or \"exit\": ")
		elif guess < "1" or len(guess) > 1:
			guess = input("Enter a number 1-9, or \"exit\": ")
		else:
			return guess

#Compare to random
def result(num, guess, count):
	if not(guess.isdigit()):
		return count

	if guess > num:
		print("Your guess was too high. Guess again.")
	elif guess < num:
		print("Your guess was too low. Guess again.")
	else:
		print("You guessed correctly!")
	count += 1
	return count

#Program start
guess = input("Guess a number between 1 and 9, or type \"exit\" to exit the game: ")

while guess != "exit":
	guess = valid(guess)
	count = result(num, guess, count)

#	print("You guessed " + guess + ".")
#	print("The random number was " + num + ".")
	
	if guess == num:
		num = str(random.randint(1,9))
		corr += 1
	
	guess = input("Guess again, or type \"exit\": ")

print("You chose to exit the game.")
print("Out of " + str(count) + " valid guesses, you correctly guessed the number " + str(corr) + " times.")