from enum import Enum

class GameState(Enum):
	TURN_START = "turn_start"
	ATTACKING = "attacking"
	MOVING = "moving"

class Game:

	def __init__(self, player):
		self._player = player
		self._state = state

	def play_turn_start(self):
		return None

	def play_attacking(self):
		player = self._player
		attacking_territory = player.pick_random_territory()
		if (attacking_territory.can_attack()):
			territory_to_attack = player.pick_neighbor_to_attack(attacking_territory)
			# TODO ....

	def play_moving(self):
		return None

	def play(self):
		if self._state == GameState.TURN_START:
			self.play_turn_start()
		elif self._state == GameState.ATTACKING:
			self.play_attacking()
		elif self._state == GameState.MOVING:
			self.play_moving()
		else:
			raise Error("Unrecognized state {}".format(self._state))
