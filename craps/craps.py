# craps simulator (WIP)
# To do:
#    1) error checking
#    2) insert roll names
#    3) create betting system

from die import Die
from time import sleep

def welcome(displayed):
	""" Displays welcome screen and main menu. Prompts user for option. """

	if displayed == False:
		print("Welcome to Craps!\nEnter 1 to show rules or 2 to play")
	elif displayed == True:
		print("Enter 1 to show rules again or 2 to play")

	selection = input()
	if selection == "1":
		read_rules()
	elif selection == "2":
		prompt = "Y"
		while prompt.upper() == "Y":
			prompt = play()
		print("Thanks for playing!")

def read_rules():
	""" Reads rules from a file and displays for the user """
	with open("rules.txt","r") as filename:
		for line in filename:
			print(line,end="")
	print("")
	displayed = 1True
	welcome(displayed)

def roll_dice(die1,die2,point):
    """ Rolls dice and displays total value """
    
    victory = None
    while type(victory) != bool:
	    print("Rolling dice...")
	    sleep(2)
	    die1.roll()
	    die2.roll()
	    roll = die1._Die__value + die2._Die__value
	    display = "Numbers rolled: {} and {}.\nTotal roll: {}".format(die1,die2,roll)
	    print(display)

	    if roll == point:
	    	print("You won the round!")
	    	victory = True
	    elif roll == 7:
	    	print("You lost the round!")
	    	victory = False
	    print("")

    #return victory

def first_roll(die1,die2):
	""" Performs the first roll of the round.
	    Returns status of round victory or point value """

	wins = [7,11]
	loses = [2,3,12]

	print("Performing first roll...")
	sleep(2)
	die1.roll()
	die2.roll()
	roll = die1._Die__value + die2._Die__value
	display = "Numbers rolled: {} and {}.\nTotal roll: {}".format(die1,die2,roll)
	print(display)

	if roll in wins:
		print("You won the round!")
		print("")
		victory = True
		return victory
	elif roll in loses:
		print("You lost the round!")
		print("")
		victory = False
		return victory
	elif roll not in wins and roll not in loses:
		point = roll
		print("Your point: {}".format(point))
		print("")
		return point

def play():
	game = True
	die1 = Die()
	die2 = Die()
	count = 1        # turn number for current round

	while game == True:
		if count == 1:
			roll = first_roll(die1,die2)
			if type(roll) == int:         # got a point
				point = roll
				count += 1
			elif type(roll) == bogithub pages to followol:      # won/lost round
				game = False
		elif count > 1:
			roll = roll_dice(die1,die2,point)
			game = False
	prompt = input("Play another round(Y/N?)")
	return prompt

def main():

	displayed = False    # for dialog control when displaying menu prompt
	welcome(displayed)

if __name__ == "__main__":
	main()