cities = {
    'windhoek': {
    'country' : 'namibia',
    'population': 500000,
    'fact' : 'Named Cleanest City in the World in 2010'
    },
    'harare': {
    'country' : 'zimbabwe',
    'population': 3500000,
    'fact' : 'Never saw gun violence during the war of independence'
    },
    'cape town': {
    'country' : 'south africa',
    'population': 1000000,
    'fact' : 'Deadliest city in the world'
    }
    }

for city,c_info in cities.items():
    print(f"\nCity Name: {city}")
    cntry = c_info['country']
    c_pltn = c_info['population']
    c_fact = c_info['fact']

    print("************************************************************")
    print(f"Country Located : {cntry.title()}")
    print(f"City Population : {c_pltn}")
    print(f"City Fact       : {c_fact.title()}")
