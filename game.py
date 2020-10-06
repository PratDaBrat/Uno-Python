#!/usr/bin/env python3
from card import *
from hand import *
from player import *
from ai_player import *
import random

class Game():
	
	def __init__(self):
		self.nplayers = 0
		self.nturn = 0
		self.isRunning = False
		self.topCard = Card("red",0)

	def getTopCard(self):
		return self.topCard

	def isPlayable(self,card):
		card.setVisibility(True)
		if card.getSpeciality():
			if "wild" in card.special:
				return True
			elif "wild" in self.topCard.special:
				return True
			elif card.color == self.topCard.color:
				return True
			else:
				return False
		else:
			if card.color == self.topCard.color or card.number == self.topCard.number:
				return True
			elif "wild" in self.topCard.special:
				return True
			else:
				return False				

	def autoPlay(self,cards):
		return cards[random.randint(0,len(cards)-1)]

	def Run(self):
		self.isRunning = True
		self.nplayers = int(input("Starting New Game... \n Input number of players: "))
		playerIDs = [x for x in range(self.nplayers)]
		pid = random.randint(0,len(playerIDs)-1)
		playerdict = {}
		players = ["" for x in range(self.nplayers)]
		rev_players = ["" for x in range(self.nplayers)]

		for i in range(len(playerIDs)):	
			if i != pid:
				playerdict[AI_Player(i)] = generateRandomHand() 

			else:
				playerdict[Player(i)] = generateRandomHand() 
			players = list(playerdict.keys())
			hands = list(playerdict.values())
			players[i].giveHand(hands[i])
		
		c = 0
		j = 0
		for player in players:
			player.playerHand = Hand(player.playerHand.cards[j*c:(j*c)+7])
			playerdict[player] = player.playerHand
			j += 1
			c = 7
			rev_players[-j] = players[j-1]

		print("\nYou are Player " + str(pid+1))
		print("\nHands dealt. Beginning game...")
		
		self.topCard = randomCardGen()
		self.topCard.setVisibility(True)
		print(self.topCard)

		check = 1

		while(self.isRunning):
			
			for i in range(len(playerIDs)):

				if checkCards(players[i]) and check == 1:
					playable = []					
					for card in players[i].playerHand.cards:
						if self.isPlayable(card):
							playable.append(card)

					if len(playable) != 0:
						if i != pid:
							playCard = self.autoPlay(playable)
							playCard.setVisibility(True)
							players[i].playCard(str(playCard))
							self.topCard = playCard
							print("Player " + str(i+1) + " played", end = " ")
							print(playCard)
						else:
							print("\nYour Turn ")
							print("Your Hand: " + str(players[i].playerHand) + "\n ")
							#c = input("Your Hand: " + str(players[i].playerHand) + " ")
							playCard = self.autoPlay(playable) #strToCard(c)
							playCard.setVisibility(True)
							players[i].playCard(str(playCard))
							self.topCard = playCard
							print("You played", end = " ")
							print(playCard)
							#if playCard in playable:
							#	players[i].playCard(playCard)
							#	self.topCard = playCard
							#else:
							#	print("You don't have that card. \n You missed your turn.")
							#	card1 = randomCardGen()
							#	players[i].giveCard(card1)
							#	print("Penalty :" + str(card1))
						if checkCards(players[i]):
							check = 1
						else:
							check = 0	

					else:
						if checkCards(players[i]):
							if i != pid:
								s = "Player " + str(i+1) + " has"
							else:
								s = "You have "
							print(s + " no playable Cards")
							card0 = randomCardGen()
							players[i].giveCard(card0)
							print(s + " picked up a Card")
							if self.isPlayable(card0):
								players[i].playCard(str(card0))
								self.topCard = card0
								print(s + " played", end = " ")
								print(card0)
							else:
								print(s + " passed turn")
						else:
							check = 0
				else:
					if i-1 == pid:
						print("You WIN !!!")
					else:
						print("Player " + str(i+2) + " wins.")
					self.isRunning = False
					break		


def checkCards(player):
	if player.hasCards():
		return True
	else:
		return False	

game = Game()
game.Run()		
