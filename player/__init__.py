from enum import Enum
import random as rand

class Strength(Enum):
	ONE_ARMY = "one_army"
	TWO_PLUS_ARMY = "two_plus_armies"

class Territory:

	def __init__(self, country, strength):
		self._country = country
		self._strength = strength

	def set_strength(self, strength):
		self._strength = strength

	def country(self):
		return self._country

	def strength(self):
		return self._strength

	def can_attack(self):
		if self._strength == Strength.TWO_PLUS_ARMY:
			return True
		else:
			return False

	def __repr__(self):
		return "Territory({} - {})".format(self._country, self._strength)

class Player:

	def __init__(self, territories):
		self._territories = territories

	def pick_neighbor_to_attack(self, territory):
		countries_owned = []
		for territory_owned in self._territories:
			countries_owned.append(territory_owned.country())
		if territory.can_attack()==True:
			country = territory.country()
			attacks = country.neighbors()
			potentials = []
			for pick in attacks:
				if pick not in countries_owned:
					potentials.append(pick)
			if len(potentials) != 0:
				attack = rand.choice(potentials)
				return attack 
			else:
				return None
		else: 
			return None

	def pick_random_territory(self):
		random_territory = rand.choice(self._territories)	
		return random_territory

	def lose_territory(self, territory):
		self._territories.remove(territory)

	def gain_territory(self, territory, strength):
		self._territories.append(territory)
		territory.set_strength(strength)
		
