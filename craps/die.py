# Die class
# Simulates dice and dice rolls

from random import randint

class Die(object):
	""" Represents one die object """

	def __init__(self,sides=6):
		self.__value = None
		self.__sides = sides

	def __str__(self):

		return str(self.__value)

	def roll(self):
		""" Rolls the die and assigns new value """

		self.__value = randint(1,self.__sides)