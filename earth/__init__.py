
class Country:

	def __init__(self, name):
		self._name = name
		self._neighbors = []

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

	


