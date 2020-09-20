from hand import *
import random

class Player():

	def __init__(self, pid = 0):
		self.playerHand = Hand()
		self.playerID = pid

	def __str__(self):
		return "Player at ID " + str(self.playerID)

	def giveHand(self, hand):
		self.playerHand = hand

	def giveCard(self, card):
		self.playerHand.cards.append(card)

	def playCard(self, c):
		for card in self.playerHand.cards:
			if c == str(card):
				self.playerHand.cards.remove(card)
				return 1
				break
			else:
				if card not in self.playerHand.cards:
					print("You don't have that card")
					return 0				

	def hasCards(self):
		if self.playerHand.isEmpty():
			return	False
		else:
			return True	



#p1 = Player()
#p1.giveHand(generateRandomHand().showCards())
#print("Your Hand: ",end = " ")
#print(p1.playerHand)
#c = input("Play a card: ")
#while(True):
#	a = p1.playCard(c)
#	if a == 0:
#		c = input("Play a valid card: ")
#	else:
#		break		
#print("Your Hand: ",end = " ")
#print(p1.playerHand)