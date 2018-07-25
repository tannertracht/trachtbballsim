import random
import names

class player():

	def __init__(self, pos):
		# Pos Guide: 1 = PG, 2 = SG, 3 = SF, 4 = PF, 5 = C
		self.firstName = names.get_first_name(gender='male')
		self.lastName = names.get_last_name()
		self.height = 0
		self.weight = 0
		self.position = pos
		self.scoring = random.randrange(1, 10, 1)
		self.passing = random.randrange(1, 10, 1)
		self.defense = random.randrange(1, 10, 1)
		if pos == 1:
			self.buildPG()
		elif pos == 2:
			self.buildSG()
		elif pos == 3:
			self.buildSF()
		elif pos == 4:
			self.buildPF()
		elif pos == 5:
			self.buildC()
		else:
			raise NameError('pos argument out of range 1 thru 5')
			
	def buildPG(self):
		self.height = self.formatHeight(random.randrange(70, 77, 1))
		self.weight = random.randrange(190, 215, 1)
	
	def buildSG(self):
		self.height = self.formatHeight(random.randrange(74, 80, 1))
		self.weight = random.randrange(190, 225, 1)
	
	def buildSF(self):
		self.height = self.formatHeight(random.randrange(76, 83, 1))
		self.weight = random.randrange(205, 240, 1)
	
	def buildPF(self):
		self.height = self.formatHeight(random.randrange(80, 83, 1))
		self.weight = random.randrange(225, 260, 1)
	
	def buildC(self):
		self.height = self.formatHeight(random.randrange(82, 88, 1))
		self.weight = random.randrange(235, 270, 1)
	
	def formatHeight(self, inches):
		if inches == 70:
			return "5'10"
		elif inches == 71:
			return "5'11"
		elif inches == 72:
			return "6'0"
		elif inches == 73:
			return "6'1"
		elif inches == 74:
			return "6'2"
		elif inches == 75:
			return "6'3"
		elif inches == 76:
			return "6'4"
		elif inches == 77:
			return "6'5"
		elif inches == 78:
			return "6'6'"
		elif inches == 79:
			return "6'7"
		elif inches == 80:
			return "6'8"
		elif inches == 81:
			return "6'9"
		elif inches == 82:
			return "6'10"
		elif inches == 83:
			return "6'11"
		elif inches == 84:
			return "7'0"
		elif inches == 85:
			return "7'1"
		elif inches == 86:
			return "7'2"
		elif inches == 87:
			return "7'3"
		elif inches == 88:
			return "7'4"
			
class BlankPlayer():

	def __init__(self, pos):
		# Pos Guide: 1 = PG, 2 = SG, 3 = SF, 4 = PF, 5 = C
		self.firstName = ''
		self.lastName = ''
		self.height = 0
		self.weight = 0
		self.position = pos
		self.scoring = 0
		self.passing = 0
		self.defense = 0
		ShootFirst = False
		PassFirst = False
		CatchAndShoot = False
		HelpDefender = False
		DenyShot = False
		DenyPass =  False

	

		

