from __init__ import Console

menu = None

def confirm():
    print("DONE")

def set_africa(value):
    print("CLICKED ON AFRICAN COUNTRY: " + value)
    menu['options']['AFRICA']['options'][value]['name'] += " (Clicked)"

def set_europe(value):
    print("CLICKED ON EUROPEAN COUNTRY: " + value)
    menu['options']['EUROPE']['options'][value]['name'] += " (Clicked)"

menu = {
    'name': "Set territories",
    'options': {
        "AFRICA": {
            'name': "Africa (10x)",
            'options': {
                "CONGO": {
                    'name': "Congo thing",
                    'value': "CONGO"

                },
                "SOUTH AFRICA": {
                    'name': "South Africa thing",
                    'value': "SOUTH AFRICA"

                }
            },
            'confirm': set_africa
        },
        "EUROPE": {
            'name': "Europe (20x)",
            'options': {
                "FRANCE": {
                    'name': "France thing",
                    'value': "FRANCE"

                },
                "GERMANY": {
                    'name': "GERMANY thing",
                    'value': "GERMANY"

                },
                "SPAIN": {
                    'name': "SPAIN thing",
                    'value': "SPAIN"

                }
            },
            'confirm': set_europe
        }
    },
    'confirm': confirm
}

cons = Console()
cons.set_menu(menu)
cons.render()
