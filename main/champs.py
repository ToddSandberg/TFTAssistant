class TFTChamp:
	def __init__(self, name, tier, type1, type2, type3=None):
		self.name = name
		self.tier = tier
		self.type1 = type1
		self.type2 = type2
		self.type3 = type3

		if self.tier == 1:
			self.copies = 39
			self.chance = 1/12
		elif self.tier == 2:
			self.copies = 26
			self.chance = 1/12
		elif self.tier == 3:
			self.copies = 21
			self.chance = 1/12
		elif self.tier == 4:
			self.copies = 13
			self.chance = 1/9
		elif self.tier == 5:
			self.copies = 10
			self.chance = 1/6

	def purchase(self):
		self.copies-=1
	def sell(self):
		self.copies+=1
	def copies(self):
		return self.copies
	def tier(self):
		return self.tier
	def chance(self, chance):
		self.chance = chance
