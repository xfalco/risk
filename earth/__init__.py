
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

	def get_neighbors(self):
		return self._neighbors

#def link(country1, country2):
#

