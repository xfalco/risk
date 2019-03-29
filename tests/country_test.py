from earth import Country

def test_country_basic():
	france = Country("france")
	germany = Country("germany")
	# let's add france as a neighbor to germany
	france.add_neighbor(germany)
	# germamy should be in france's neighbors
	assert germany in france.get_neighbors()
	# now add spain as another neighbor
	spain = Country("spain")
	france.add_neighbor(spain)
	assert spain in france.get_neighbors()
	assert france.get_neighbors() == [germany, spain]
	belgium = Country("belgium")
	italy = Country("italy")
	france.add_neighbors([belgium, italy])
	assert italy in france.get_neighbors()