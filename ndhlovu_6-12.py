users = {
    'aeinstein': {
    'first': 'albert',
    'last': 'einstein',
    'location': 'princeton',
    'fav_food': 'fish'
    },
    'mcurie': {
    'first': 'marie',
    'last': 'curie',
    'location': 'paris',
    'fav_food': 'lobsters'
    },

    'phx': {
    'first': 'phoenix',
    'last': 'sultan',
    'location': 'whindhoek',
    'fav_food': 'kapana'
    }
    }

for username,user_info in users.items():
    print(f"\n\t\tUsername : {username}")
    print('****************************************************')
    location   = (f"{user_info['location']}")
    fav_food   = (f"{user_info['fav_food']}")
    full_name = (f"{user_info['first']} {user_info['last']}")

    print(f"Full Name      : {full_name.title()}")
    print(f"Location       : {location.title()}")
    print(f"Favourite Food : {fav_food.title()}")
