from earth import Country, Continent, link

def test_country_basic():
	france = Country("france")
	germany = Country("germany")
	# let's add france as a neighbor to germany
	france.add_neighbor(germany)
	# germamy should be in france's neighbors
	assert germany in france.neighbors()
	# now add spain as another neighbor
	spain = Country("spain")
	france.add_neighbor(spain)
	assert spain in france.neighbors()
	assert france.neighbors() == [germany, spain]
	belgium = Country("belgium")
	italy = Country("italy")
	france.add_neighbors([belgium, italy])
	assert italy in france.neighbors()

def test_country_linking():
	france = Country("france")
	germany = Country("germany")
	link(france, germany)
	print(france.neighbors())
	print(germany.neighbors())
	# expect france to be a neighbor of germany
	# and vice versa
	assert germany in france.neighbors()
	assert france in germany.neighbors()

def test_continent():
	france = Country("france")
	germany = Country("germany")
	europe = Continent("Europe", 5)
	europe.add_countries([france, germany])
	assert europe.countries() == [france, germany]