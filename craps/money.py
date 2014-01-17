# money class

class Money(object):
	""" Represents player's wallet and bets """
	def __init__(self):
		
		self.wallet = 10000
		self.bet_amt = 0
		self.bet_type = None
	
	def __str__(self):

		return str(self.wallet)

	def betting(self):
		""" Allows the player to place a bet """

		bets = ["pass","no pass","no bet"]
		self.bet_type = None
		self.bet_amt = 0

		# select bet type
		while self.bet_type == None:
			print("Place a bet (pass/no pass/no bet)")
			prompt = input("> ")
			if prompt.lower() in bets:
				self.bet_type = prompt.lower()
				print(prompt.capitalize(),"selected.")
				print("")

		# select bet amount
		if self.bet_type == "pass" or self.bet_type == "no pass":
			while self.bet_amt == 0:
				print("Bet how much?")
				amount = int(input("> "))
				self.bet_amt = amount