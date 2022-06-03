people = {
    'seb': {
    'first_name':'David',
    'last_name':'Sebulon',
    'age':'30',
    'city':'Windhoek'},
    'nim': {
    'first_name':'Oscar',
    'last_name':'Bowora',
    'age':'19',
    'city':'Walvis'},
    'cas': {
    'first_name':'Casper',
    'last_name':'Novest',
    'age':'22',
    'city':'Luderitz'}
    }

for name, user_info in people.items():
    print(f"\nUsername: {name}")
    f_name = f"{user_info['first_name']} {user_info['last_name']}"
    r_ages= f"{user_info['age']}"
    location = user_info['city']

    print("************************************************************")
    print(f"\tFull Name: {f_name.title()}")
    print(f"\tAge      : {r_ages}")
    print(f"\tLocation : {location.title()}")
