fav_numbers = {
    'tino': {
    'fav_num1': 30,
    'fav_num2': 3,},
    'nim': {
    'fav_num1': 30,
    'fav_num2': 3,},
    'cas': {
    'fav_num1': 4,
    'fav_num2': 6,}
    }

for name,num in fav_numbers.items():
    print(f"\nName: {name.title()}")
    fav_num1 = num['fav_num1']
    fav_num2 = num['fav_num2']


    print('*********************************************')
    print(f"\tFavourite Number One : {fav_num1}")
    print(f"\tFavourite Number One : {fav_num2}")
