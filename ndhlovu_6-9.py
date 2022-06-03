people = {
    'seb': {
    'fav_place1':'Namibia',
    'fav_place2':'Nigeria',
    'fav_place3':'Sudan'},
    'nim': {
    'fav_place1':'Cape Town',
    'fav_place2':'USA',
    'fav_place3':'Uk'},
    'cas': {
    'fav_place1':'Mozambique',
    'fav_place2':'Angola',
    'fav_place3':'Malawi'}
    }

for name, user_info in people.items():
    print(f"\nUsername: {name}")
    fav_place_1 = f"{user_info['fav_place1']}"
    fav_place_2= f"{user_info['fav_place2']}"
    fav_place_3 = user_info['fav_place3']

    print("************************************************************")
    print(f"\tFavourite Place One    : {fav_place_1.title()}")
    print(f"\tFavourite Place Two    : {fav_place_2.title()}")
    print(f"\tFavourite Place Three  : {fav_place_3.title()}")
