
class Country:

	def __init__(self, name):
		self._name = name
		self._neighbors = []

	def name(self):
		return self._name

	def add_neighbor(self, neighbor):
		if neighbor not in self._neighbors:
			self._neighbors.append(neighbor)

	def add_neighbors(self, neighbors):
		for neighbor in neighbors:
			self.add_neighbor(neighbor)

	def neighbors(self):
		return self._neighbors

	def __repr__(self):
		return "Country(\"{}\")".format(self._name)

def link(country1, country2):
	country1.add_neighbor(country2)
	country2.add_neighbor(country1)


class Continent:

	def __init__(self, name, value):
		self._name = name
		self._value = value
		self._countries = []

	def add_countries(self, countries):
		for country in countries:
			self._countries.append(country)

	def countries(self):
		return self._countries

	def name(self):
		return self._name

# COUNTRIES

# Europe
ICELAND = Country("Iceland")
SCANDINAVIA = Country("Scandinavia")
GREAT_BRITAIN = Country("Great Britain")
NORTHERN_EUROPE = Country("Northern Europe")
WESTERN_EUROPE = Country("Western Europe")
SOUTHERN_EUROPE = Country("Southern Europe")
RUSSIA = Country("Russia")

#North America
GREENLAND = Country("Greenland")
ALASKA = Country("Alaska")
NORTHWEST_TERRITORY = Country("Northwest territory")
ALBERTA = Country("Alberta")
ONTARIO = Country("Ontario")
EASTERN_CANADA = Country("Eastern Canada")
WESTERN_US = Country("Western US")
EASTERN_US = Country("Eastern US")
CENTRAL_AMERICA = Country("Central America")

#South America
VENEZUELA = Country("Venezuela")
BRAZIL = Country("Brazil")
PERU = Country("Peru")
ARGENTINA = Country("Argentina")

#North Africa
NORTH_AFRICA = Country("North Africa")
EGYPT = Country("Egypt")
CENTRAL_AFRICA = Country("Central Africa")
EAST_AFRICA = Country("East Africa")
SOUTH_AFRICA = Country("South Africa")
MADAGASCAR = Country("Madagascar")

#Asia
MIDDLE_EAST = Country("Middle East")
AFGHANISTAN = Country("Afghanistan")
URAL = Country("Ural")
SIBERIA = Country("Siberia")
YAKUTSK = Country("Yakutz")
KAMCHATKA = Country("Kamchatka")
IRKUTSK = Country("Irkutsk")
MONGOLIA = Country("Mongolia")
JAPAN = Country("Japan")
CHINA = Country("China")
INDIA = Country("India")
SOUTHEAST_ASIA = Country("Southeast Asia")

#Australia
EASTERN_AUSTRALIA = Country("Eastern Australia")
WESTERN_AUSTRALIA = Country("Western Australia")
INDONESIA = Country("Indonesia")
NEW_GUINEA = Country("New Guinea")

# link all of them
link(ICELAND, GREENLAND)
link(ICELAND, SCANDINAVIA)
link(ICELAND, GREAT_BRITAIN)
link(GREAT_BRITAIN, SCANDINAVIA)
link(GREAT_BRITAIN, NORTHERN_EUROPE)
link(GREAT_BRITAIN, WESTERN_EUROPE)
link(SCANDINAVIA, NORTHERN_EUROPE)
link(SCANDINAVIA, RUSSIA)
link(RUSSIA, NORTHERN_EUROPE)
link(RUSSIA, SOUTHERN_EUROPE)
link(SOUTHERN_EUROPE, NORTHERN_EUROPE)
link(WESTERN_EUROPE, NORTHERN_EUROPE)
link(WESTERN_EUROPE, SOUTHERN_EUROPE)
link(WESTERN_EUROPE, NORTH_AFRICA)
link(SOUTHERN_EUROPE, NORTH_AFRICA)
link(SOUTHERN_EUROPE, EGYPT)
link(SOUTHERN_EUROPE, MIDDLE_EAST)

link(GREENLAND, EASTERN_CANADA)
link(GREENLAND, ONTARIO)
link(GREENLAND, NORTHWEST_TERRITORY)
link(NORTHWEST_TERRITORY, ALBERTA)
link(NORTHWEST_TERRITORY, ALASKA)
link(NORTHWEST_TERRITORY, ONTARIO)
link(ALASKA, KAMCHATKA)
link(ALASKA, ALBERTA)
link(ALBERTA, ONTARIO)
link(ALBERTA, WESTERN_US)
link(ONTARIO, EASTERN_CANADA)
link(ONTARIO, EASTERN_US)
link(EASTERN_CANADA, EASTERN_US)
link(WESTERN_US, EASTERN_US)
link(WESTERN_US, CENTRAL_AMERICA)
link(EASTERN_US, CENTRAL_AMERICA)
link(CENTRAL_AMERICA, VENEZUELA)

link(VENEZUELA, BRAZIL)
link(VENEZUELA, PERU)
link(PERU, BRAZIL)
link(PERU, ARGENTINA)
link(ARGENTINA, BRAZIL)
link(BRAZIL, NORTH_AFRICA)

link(NORTH_AFRICA, EGYPT)
link(NORTH_AFRICA, EAST_AFRICA)
link(NORTH_AFRICA, CENTRAL_AFRICA)
link(EGYPT, MIDDLE_EAST)
link(EGYPT, EAST_AFRICA)
link(EAST_AFRICA, CENTRAL_AFRICA)
link(CENTRAL_AFRICA, SOUTH_AFRICA)
link(SOUTH_AFRICA, MADAGASCAR)
link(MADAGASCAR, EAST_AFRICA)

link(RUSSIA, URAL)
link(RUSSIA, AFGHANISTAN)
link(RUSSIA, MIDDLE_EAST)
link(MIDDLE_EAST, INDIA)
link(MIDDLE_EAST, AFGHANISTAN)
link(AFGHANISTAN, CHINA)
link(AFGHANISTAN, INDIA)
link(AFGHANISTAN, CHINA)
link(AFGHANISTAN, URAL)
link(URAL, SIBERIA)
link(URAL, CHINA)
link(SIBERIA, YAKUTSK)
link(SIBERIA, IRKUTSK)
link(SIBERIA, MONGOLIA)
link(SIBERIA, CHINA)
link(YAKUTSK, KAMCHATKA)
link(KAMCHATKA, JAPAN)
link(JAPAN, MONGOLIA)
link(YAKUTSK, IRKUTSK)
link(KAMCHATKA, IRKUTSK)
link(IRKUTSK, MONGOLIA)
link(MONGOLIA, CHINA)
link(CHINA,INDIA)
link(INDIA, AFGHANISTAN)
link(INDIA, MIDDLE_EAST)
link(INDIA, SOUTHEAST_ASIA)
link(SOUTHEAST_ASIA, CHINA)

link(INDONESIA, SOUTHEAST_ASIA)
link(INDONESIA, NEW_GUINEA)
link(INDONESIA, WESTERN_AUSTRALIA)
link(NEW_GUINEA, WESTERN_AUSTRALIA)
link(NEW_GUINEA, EASTERN_AUSTRALIA)
link(WESTERN_AUSTRALIA, EASTERN_AUSTRALIA)

# CONTINENTS

# continents
EUROPE = Continent("Europe", 5)
NORTH_AMERICA = Continent("North America", 5)
SOUTH_AMERICA = Continent("South America", 2)
AFRICA = Continent("Africa", 3)
ASIA = Continent("Asia", 7)
AUSTRALIA = Continent("Australia", 2)

EUROPE.add_countries([WESTERN_EUROPE, SOUTHERN_EUROPE, ICELAND, SCANDINAVIA, GREAT_BRITAIN, NORTHERN_EUROPE, RUSSIA])
NORTH_AMERICA.add_countries([ALASKA, NORTHWEST_TERRITORY, GREENLAND, ALBERTA, ONTARIO, EASTERN_CANADA, WESTERN_US, EASTERN_US, CENTRAL_AMERICA])
SOUTH_AMERICA.add_countries([VENEZUELA, BRAZIL, PERU, ARGENTINA])
AFRICA.add_countries([NORTH_AFRICA, EGYPT, EAST_AFRICA, CENTRAL_AFRICA, SOUTH_AFRICA, MADAGASCAR])
ASIA.add_countries([MIDDLE_EAST, AFGHANISTAN, URAL, SIBERIA, YAKUTSK, KAMCHATKA, IRKUTSK, MONGOLIA, JAPAN, CHINA, INDIA, SOUTHEAST_ASIA])
AUSTRALIA.add_countries([INDONESIA, NEW_GUINEA, WESTERN_AUSTRALIA, EASTERN_AUSTRALIA])
# global variables
CONTINENTS = [EUROPE,NORTH_AMERICA, SOUTH_AMERICA, AFRICA, ASIA, AUSTRALIA]

COUNTRIES = []
for continent in CONTINENTS:
	COUNTRIES += continent.countries()
