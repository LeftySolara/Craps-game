# money class

class Money(object):
	""" Represents player's wallet and bets """
	def __init__(self):
		
		self.wallet = 10000    # amount of money in wallet
		self.bet_amt = 0       # size of bet
		self.bet_type = None   # type of bet placed
		self.bets = 0          # number of bets
	
	def __str__(self):

		return str(self.wallet)

	def betting(self):
		""" Allows the player to place a bet """

		bets = ["pass","no pass","no bet"]
		self.bet_type = None
		self.bet_amt = 0
		while self.bet_type == None:
			print("Place a bet (pass/no pass/no bet)")
			kind = input("> ")
			if kind.lower() in bets:
				self.bet_type = kind.lower()
				print(kind.capitalize(),"selected.")
				print("")
		if self.bet_type == "pass" or self.bet_type == "no pass":
			while self.bet_amt == 0:
				print("Bet how much?")
				amount = int(input("> "))
				self.bet_amt = amount