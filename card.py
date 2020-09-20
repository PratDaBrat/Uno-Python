import random

class Colors():
	def __init__(self):
		self.colors = ["","red","green","yellow","blue"]

class Numbers():
	def __init__(self):
		self.numbers = ["",0,1,2,3,4,5,6,7,8,9]	

class Speciality():
	def __init__(self):
		self.speciality = ["","skip","+4 and wild","+2","wild","reverse"]		


class Card():

	def __init__(self, color, number, special_stat = False, special = "", visibility = True): #default False	
		self.color = color
		self.number = number
		self.special_stat = special_stat
		self.special = special
		self.visibility = visibility

		#checks
		if special_stat == False and (color == "" or number == ""):
			raise Exception("Invalid card")
		if special_stat == False and special != "":
			raise Exception("Invalid card")
		if special_stat == True and special == "":
			raise Exception("Invalid card")		
		if color not in Colors().colors:
			raise Exception("Invalid card")
		if number not in Numbers().numbers:
			raise Exception("Invalid card")
		if 	special not in Speciality().speciality:
			raise Exception("Invalid card")

	def __str__(self):
		if self.visibility:
			if self.special_stat == True:
				if self.color == "":
					a = "{}".format(self.special)
				else:
					a = "{} of {}".format(self.special,self.color)
			else:
				a = "{} of {}".format(self.number,self.color)	
			return a 
		else:
			return "Card is face down."	

	def getVisibility(self):
		return self.visibility

	def setVisibility(self,v):
		self.visibility = v

	def getColor(self):
		return self.color

	def setColor(self,c):
		if c in Colors().colors:
			self.color = c
		else:
			self.color = ""
			raise Exception("invalid color")	

	def getNumber(self):
		return self.number

	def setNumber(self,n):
		if n in Numbers().numbers:
			self.number = n
		else:
			self.number = ""
			raise Exception("invalid number")				

	def getSpeciality(self):
		return self.special_stat

	def setSpeciality(self,s):
		self.special_stat = s

def isPrime(a):
	count = 0
	for i in range(2,a+1):
		if a % i != 0:
			count += 1	
	if count != 0:
		return False
	else:
	 	return True			

def strToCard(c):
	if "wild" in c.split(" "):
		if len(c.split(" ")) == 1:
			card = Card("","",True,"wild")
		else:
			card = Card("","",True,"+4 and wild")
	elif "wild" not in c.split(" "):
		for color in Colors().colors:
			if color == c.split(" ")[2] and len(c.split(" ")[0]) == 1:
				card = Card(color, int(c.split(" ")[0]))
			elif color == c.split(" ")[2] and len(c.split(" ")[0]) != 1:
				card = Card(color,"",True,c.split(" ")[0])
	else:
		card = Card("","")
		raise Exception("Invalid Card")			
	return card		

def randomCardGen():
	color = Colors().colors[random.randint(1,4)]
	number = Numbers().numbers[random.randint(1,10)]
	if isPrime(random.randint(0,30)):
		special_stat = True
		special = Speciality().speciality[random.randint(1,5)]
		if special.find("wild") != -1:
			color = ""
			number = ""
		else:
			number = ""	
	else:
		special_stat = False
		special = ""

	return Card(color,number,special_stat,special)


#card1 = randomCardGen()
#card1.setVisibility(True)
#print(card1)
