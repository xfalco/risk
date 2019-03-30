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

	def __init__(self):
		self._territories = {}

	def pick_neighbor_to_attack(self, territory):
		if territory.can_attack()==True:
			country = territory.country()
			attacks = country.neighbors()
			potentials = []
			for pick in attacks:
				if pick.name() not in self._territories:
					potentials.append(pick)
			if len(potentials) != 0:
				attack = rand.choice(potentials)
				return attack 
			else:
				return None
		else: 
			return None

	def pick_random_territory(self):
		random_territory = rand.choice(list(self._territories.values()))	
		return random_territory

	def territory_for_country(self, country):
		if country.name() in self._territories:
			return self._territories[country.name()]
		else:
			return None

	def lose_country(self, country):
		country_name = country.name()
		del self._territories[country_name]

	def gain_country(self, country, strength):
		new_territory = Territory(country, strength)
		self._territories[country.name()] = new_territory
		
