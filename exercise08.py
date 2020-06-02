"""
From https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock
"""

#With while loops
play = "y"

#Initialize p1 and p2 outside main loop to avoid redundant instructions
p1 = "x"
while p1.isdigit() == False:
	p1 = input("Player One, pick rock [1], paper [2], or scissors [3] by typing in the corresponding number: ")

p2 = "x"
while p2.isdigit() == False:
	p2 = input("Player Two, pick rock [1], paper [2], or scissors [3] by typing in the corresponding number: ")

#Start main loop
while play == "y":
	while p1 != "1" and p1 != "2" and p1 != "3":
		p1 = input("Player One, please enter 1, 2, or 3: ")
	while p2 != "1" and p2 != "2" and p2 != "3":
		p2 = input("Player Two, please enter 1, 2, or 3: ")

#Review the logic later x_x		
	if p1 == p2:
		print("You tied!")
	elif p1 > p2:
		if p1 == "3" and p2 == "1":
			print("Player Two wins!")
		else:
			print("Player One wins!")
	elif p1 < p2 and p1 == "1" and p2 == "3":
		print("Player One wins!")
	else:
		print("Player Two wins!")

#Re-initialize variables for next iteration
	play = input("Would you like to play again? Press [Y] for yes, or hit any other key to exit: ")
	if play == "Y":
		play = play.lower()
	
	p1 = "x"
	p2 = "x"

#End game	
print("Okay! Goodbye!")

#With functions

#Validate input
def valid_rps(player):
	while player.isdigit == False:
		player = input("Please enter 1, 2, or 3: ")
	while player != "1" and player != "2" and player != "3":
		player = input("Please enter 1, 2, or 3: ")
	return player

#Calculate result
def result(p1, p2):
	if p1 == p2:
		print("You tied!")
	if p1 > p2:
		if p1 == "3" and p2 == "1":
			print("Player Two wins!")
		else:
			print("Player One wins!")
	if p1 < p2:
		if p1 == "1" and p2 == "3":
			print("Player One wins!")
		else:
			print("Player Two wins!")

#Gameplay
def replay(p1, p2):
	p1 = input("Player One, enter your choice: ")
	p1 = valid_rps(p1)
	
	p2 = input("Player Two, enter your choice: ")
	p2 = valid_rps(p2)
	
	result(p1, p2)

#Initialize variables
play = "y"
p1 = "x"
p2 = "x"

print("In this game of Rock, Paper, Scissors, enter [1] for rock, [2] for paper, or [3] for scissors.")

replay(p1, p2)

while play == "y":	
	play = input("Would you like to play again? Press [Y] for yes, or hit any other key to exit: ")
	if play == "Y" or play == "y":
		play = play.lower()	
		replay(p1, p2)

#End game	
print("Okay! Goodbye!")