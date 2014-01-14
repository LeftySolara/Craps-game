# money class

class money(object):
	""" Represents player's wallet and bets """
	def __init__(self):
		
		self.wallet = 10000    # amount of money in wallet
		self.bet_amt = 0       # size of bet
		self.bet_type = None   # type of bet placed
		self.bets = 0          # number of bets
	
	def __str__(self):

		return self.wallet

	def addition(self):
		""" Adds money to wallet """

	def place(self,bet,kind):
		""" Places bet of specified type and amount """

		self.bet_amt = bet
		self.wallet -= self.bet_amt
		self.bet_type = kind