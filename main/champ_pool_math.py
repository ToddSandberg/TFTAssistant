from champs import TFTChamp

class TFTChampPool:
	def __init__(self):
		self.arr={}
		temp = TFTChamp(name, tier, type1, type2, type3)
		self.arr[name]=temp
		self.level = 1
		self.tier_chances = [[1.0, 0.0, 0.0, 0.0, 0.0],
							[1.0,0.0,0.0,0.0,0.0],
							[.70,.30,0.0,0.0,0.0],
							[.55,.30,.15,0.0,0.0],
							[.40,.30,.25,.05,0.0],
							[.29,.295,.31,.10,.005],
							[.24,.28,.31,.15,.02],
							[.20,.24,.31,.20,.05],
							[.10,.19,.31,.30,.10]]

	def purchase(self, name):
		self.arr[name].purchase()

	def sell(self, name):
		self.arr[name].sell()

	def level_up(self):
		self.level+=1

	def calculate_champ_chance(self,name):
		copies = self.arr[name].copies()
		tier = self.arr[name].tier()
		tier_chance = self.tier_chances[self.level-1][tier-1]

		total=0
		for key in self.arr.keys():
			if self.arr[key].tier() != tier:
				continue
			total+=self.arr[key].copies()

		return tier_chance*copies/total

	def calculate_most_likely_champs(self):
		one = [None,0.0]
		two = [None,0.0]
		three = [None,0.0]
		four = [None,0.0]
		five = [None,0.0]
		for key in self.arr.keys():
			chance = calculate_champ_chance(key)
			self.arr[key].chance(chance)
			if chance > one[1]:
				five = four
				four = three
				three = two
				two = one
				one[1] = chance
				one[0] = key
			elif chance > two[1]:
				five = four
				four = three
				three = two
				two[1] = chance
				two[0] = key
			elif chance > three[1]:
				five = four
				four = three
				three[1] = chance
				three[0] = key
			elif chance > four[1]:
				five = four
				four[1] = chance
				four[0] = key
			elif chance > five[1]:
				five[1] = chance
				five[0] = key
		return [one,two,three,four,five]