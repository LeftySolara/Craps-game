# Simple craps simulator

from die import Die
from money import Money
from time import sleep

def welcome(displayed):
	""" Displays welcome screen and main menu. Prompts user for option. """

	if displayed == False:    # rules have not been displayed
		print("Welcome to Craps!\nEnter 1 to show rules or 2 to play")
	elif displayed == True:   # rules have been displayed
		print("Enter 1 to show rules again or 2 to play")

	selection = input()
	if selection == "1":
		read_rules()
	elif selection == "2":
		player = spawn()
		prompt = "Y"
		while prompt.upper() == "Y":
			prompt = play(player)
		print("Thanks for playing!")
	else:
		print("Invalid option. Exiting...")

def read_rules():
	""" Reads rules from a file and displays for the user """
	with open("rules.txt","r") as filename:
		for line in filename:
			print(line,end="")
	print("")
	displayed = True
	welcome(displayed)

def roll_dice(die1,die2,point,player):
    """ Rolls dice and displays total value """

    victory = None
    while type(victory) != bool:
	    print("Rolling dice...")
	    sleep(3)
	    die1.roll()
	    die2.roll()
	    roll = die1._Die__value + die2._Die__value
	    display = "Numbers rolled: {} and {}.\nTotal roll: {}".format(die1,die2,roll)
	    print(display)

	    if roll == point:
	    	print("You won the round!")
	    	print("You gained ${}".format(player.bet_amt))
	    	player.wallet += player.bet_amt
	    	victory = True
	    elif roll == 7:
	    	print("You lost the round!")
	    	print("You lost ${}".format(player.bet_amt))
	    	player.wallet -= player.bet_amt
	    	victory = False
	    print("Your wallet: ${}".format(player.wallet))
	    print("")

def first_roll(die1,die2,player):
	""" Performs the first roll of the round.
	    Returns status of round victory or point value """

	print("Your wallet: ${}".format(player.wallet))

	wins = [7,11]
	loses = [2,3,12]

	print("Performing first roll...")
	sleep(3)
	die1.roll()
	die2.roll()
	roll = die1._Die__value + die2._Die__value
	display = "Numbers rolled: {} and {}.\nTotal roll: {}".format(die1,die2,roll)
	print(display)

	if roll in wins:
		print("You rolled a natural!")
		if player.bet_type == "pass":
			player.wallet += player.bet_amt
			print("You gained ${}".format(player.bet_amt))
		elif player.bet_type == "no pass":
			player.wallet -= player.bet_amt
			print("You lost ${}".format(player.bet_amt))
		elif player.bet_type == "no bet":
			pass
		print("Your wallet: ${}".format(player.wallet))
		victory = True
		return victory

	elif roll in loses:
		print("You crapped out!")
		if player.bet_type == "pass":
			player.wallet -= player.bet_amt
			print("You lost ${}".format(player.bet_amt))
		elif player.bet_type == "no pass":
			player.wallet += player.bet_amt
			print("You gained ${}".format(player.bet_amt))
		elif player.bet_type == "no bet":
			pass
		print("Your wallet: ${}".format(player.wallet))
		victory = False
		return victory

	elif roll not in wins and roll not in loses:
		point = roll
		print("Your point: {}".format(point))
		print("")
		return point

def spawn():
	""" Initialized values for player's wallet. """

	player = Money()
	return player

def play(player):
	game = True
	die1 = Die()
	die2 = Die()
	turn = 1        # turn number for current round

	while game == True:
		if turn == 1:
			player.betting()
			roll = first_roll(die1,die2,player)
			if type(roll) == int:         # got a point
				point = roll
				turn += 1
			elif type(roll) == bool:      # won/lost round
				game = False
		elif turn > 1:
			roll = roll_dice(die1,die2,point,player)
			game = False
	prompt = input("Play another round(Y/N?)")
	return prompt

def main():

	displayed = False
	welcome(displayed)

if __name__ == "__main__":
	main()