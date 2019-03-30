from enum import Enum
from console import Console
import random as rand
from player import Strength, Territory
from earth import CONTINENTS

class GameState(Enum):
	TURN_START = "turn_start"
	ATTACKING = "attacking"
	MOVING = "moving"

class Game:

	def __init__(self, player, console):
		self._player = player
		self._state = GameState.TURN_START
		self._console = console

	def play_turn_start(self):
		def label_for_country(country):
			territory = self._player.territory_for_country(country)
			suffix = ""
			if territory is None:
				suffix = " (not owned)"
			elif territory.can_attack():
				suffix = " (2+ armies)"
			else:
				suffix = " (1 army)"
			return country.name() + suffix
		def label_for_continent(continent):
			num_countries_owned = 0
			for country in continent.countries():
				territory = self._player.territory_for_country(country)
				if territory is not None:
					num_countries_owned += 1
			return continent.name() + " ({} owned)".format(num_countries_owned)
		menu = {
			'name': "Set territories",
			'options': {}
		}
		for continent in CONTINENTS:
			def click_country(country, continent=continent):
				territory = self._player.territory_for_country(country)
				if territory is None:
					self._player.gain_country(country, Strength.ONE_ARMY)
				elif territory.strength() == Strength.ONE_ARMY:
					territory.set_strength(Strength.TWO_PLUS_ARMY)
				else:
					self._player.lose_country(country)
				menu['options'][continent.name()]['name'] = label_for_continent(continent)
				menu['options'][continent.name()]['options'][country.name()]['name'] = label_for_country(country)
				return True		
			menu['options'][continent.name()] = {
				'name': label_for_continent(continent),
				'options': {},
				'confirm': click_country
			}
			for country in continent.countries():
				menu['options'][continent.name()]['options'][country.name()] = {
					'name': label_for_country(country),
					'value': country
				}
		def done():
			print("DONE ENTERING COUNTRIES :)")
			self._state = GameState.ATTACKING
		menu['confirm'] = done
		self._console.set_menu(menu)
		self._console.render()
		done()

	def play_attacking(self):
		pick=rand.choice(["H", "T"])
		if pick == "H":
			print("SKIPPING ATTACK")
			self._state = GameState.MOVING
		else:
			player = self._player
			attacking_territory = player.pick_random_territory()
			neighbor_to_attack = player.pick_neighbor_to_attack(attacking_territory)
			if neighbor_to_attack is None:
				print("Not attacking this turn")
			else:
				WON_1_ARMY = "WON_1_ARMY"
				WON_2_ARMIES = "WON_2_ARMIES"
				LOST = "LOST"
				def answer(outcome):
					if outcome == WON_1_ARMY:
						print("{} won {} with 1 army".format(attacking_territory, neighbor_to_attack))
						player.gain_country(neighbor_to_attack, Strength.ONE_ARMY)
					elif outcome == WON_2_ARMIES:
						print("{} won {} with 2+ armies".format(attacking_territory, neighbor_to_attack))
						player.gain_country(neighbor_to_attack, Strength.TWO_PLUS_ARMY)
					else:
						print("{} attacked {} but lost".format(attacking_territory, neighbor_to_attack))
					attacking_territory.set_strength(Strength.ONE_ARMY)
				menu = {
					'name': "{} attacks {}".format(attacking_territory, neighbor_to_attack),
					'options': {
						"LOST": {
							'name': "lost",
							'value': LOST,
						},
						"WON_2_ARMIES": {
							'name': "won (2+ armies left)",
							'value': WON_2_ARMIES,
						},
						"WON_1_ARMY": {
							'name': "won (1 army left)",
							'value': WON_1_ARMY,
						},
					},
					'confirm': answer
				}
				self._console.set_menu(menu)
				self._console.render()

	def play_moving(self):
		print("NOT MOVING")
		self._state = GameState.TURN_START

	def play(self):
		while (True):
			if self._state == GameState.TURN_START:
				self.play_turn_start()
			elif self._state == GameState.ATTACKING:
				self.play_attacking()
			elif self._state == GameState.MOVING:
				self.play_moving()
			else:
				raise Error("Unrecognized state {}".format(self._state))