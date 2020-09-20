from card import *

class Hand():
	def __init__(self,cards = []):
		self.cards = cards

	def __str__(self):
		a = "* "
		for card in self.cards:
			if card == self.cards[-1]:
				a += str(card) + " *"
			else:	
				a += str(card) + ", "
		return a

	def showCards(self):
		for card in self.cards:
			card.setVisibility(True)
		return Hand(self.cards)

	def isEmpty(self):
		if self.cards == []:
			return True
		else:
			return False		


def generateRandomHand():
	hand = Hand()
	cards = hand.cards
	for i in range(0,7):
		card = randomCardGen()
		cards.append(card)
	newhand = Hand(cards)
	return newhand	
	

#hand = generateRandomHand().showCards()
#print(hand)