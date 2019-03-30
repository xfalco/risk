from earth import BRAZIL, PERU, NORTH_AFRICA, VENEZUELA, ARGENTINA
from player import Territory, Strength, Player
import random as rand

def test_territory_basic():
	brazil_territory = Territory(BRAZIL, Strength.ONE_ARMY)
	assert brazil_territory.can_attack() == False
	brazil_territory.set_strength(Strength.TWO_PLUS_ARMY)
	assert brazil_territory.can_attack() == True

def test_player_attacking():
	player = Player()
	player.gain_country(BRAZIL, Strength.TWO_PLUS_ARMY)
	player.gain_country(PERU, Strength.TWO_PLUS_ARMY)
	player.gain_country(VENEZUELA, Strength.ONE_ARMY)
	player.gain_country(ARGENTINA, Strength.TWO_PLUS_ARMY)
	territories = list(player._territories.values())
	assert len(territories) == 4
	random_territory = player.pick_random_territory()
	brazil_territory = player._territories[BRAZIL.name()]
	assert random_territory in territories
	country_to_attack = player.pick_neighbor_to_attack(brazil_territory)
	assert country_to_attack == NORTH_AFRICA
	peru_territory = player._territories[PERU.name()]
	no_country_to_attack = player.pick_neighbor_to_attack(peru_territory)
	assert no_country_to_attack == None

def test_gain_lose_territory():
	player = Player()
	player.gain_country(BRAZIL, Strength.TWO_PLUS_ARMY)
	player.gain_country(PERU, Strength.TWO_PLUS_ARMY)
	player.gain_country(VENEZUELA, Strength.ONE_ARMY)
	player.gain_country(ARGENTINA, Strength.TWO_PLUS_ARMY)
	territories = list(player._territories.values())
	assert len(territories) == 4
	player.lose_country(BRAZIL)
	assert BRAZIL.name() not in player._territories
	player.gain_country(BRAZIL,Strength.ONE_ARMY)
	assert BRAZIL.name() in player._territories
	assert player._territories[BRAZIL.name()].can_attack() == False