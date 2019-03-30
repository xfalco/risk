from earth import BRAZIL, PERU, NORTH_AFRICA, VENEZUELA, ARGENTINA
from player import Territory, Strength, Player
import random as rand

def test_territory_basic():
	brazil_territory = Territory(BRAZIL, Strength.ONE_ARMY)
	assert brazil_territory.can_attack() == False
	brazil_territory.set_strength(Strength.TWO_PLUS_ARMY)
	assert brazil_territory.can_attack() == True

def test_player_attacking():
	brazil_territory = Territory(BRAZIL, Strength.TWO_PLUS_ARMY)
	peru_territory = Territory(PERU, Strength.TWO_PLUS_ARMY)
	venezuela_territory = Territory(VENEZUELA, Strength.ONE_ARMY)
	argentina_territory = Territory(ARGENTINA, Strength.TWO_PLUS_ARMY)
	territories = [brazil_territory, peru_territory, venezuela_territory, argentina_territory]
	player = Player(territories)
	random_territory = player.pick_random_territory()
	assert random_territory in territories
	country_to_attack = player.pick_neighbor_to_attack(brazil_territory)
	assert country_to_attack == NORTH_AFRICA
	no_country_to_attack = player.pick_neighbor_to_attack(peru_territory)
	assert no_country_to_attack == None

def test_gain_lose_territory():
	brazil_territory = Territory(BRAZIL, Strength.TWO_PLUS_ARMY)
	peru_territory = Territory(PERU, Strength.TWO_PLUS_ARMY)
	venezuela_territory = Territory(VENEZUELA, Strength.ONE_ARMY)
	argentina_territory = Territory(ARGENTINA, Strength.TWO_PLUS_ARMY)
	territories = [brazil_territory, peru_territory, venezuela_territory, argentina_territory]
	player = Player(territories)
	player.lose_territory(brazil_territory)
	assert brazil_territory not in territories
	player.gain_territory(brazil_territory,Strength.ONE_ARMY)
	assert brazil_territory in territories
	assert brazil_territory.can_attack() == False