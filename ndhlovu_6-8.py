pets = {
    'cat': {
    'anim_type':'House Pet',
    'owner':'Sebulon'},
    'dog': {
    'anim_type':'Oscar',
    'owner':'Bowora'},
    'rabbit': {
    'anim_type':'Farm Pet',
    'owner':'Novest'}
    }

for dog_type, pet_info in pets.items():
    print(f"\nPet Type: {dog_type}")
    pet_owner = f"{pet_info['owner']}"
    pet_type = pet_info['anim_type']

    print("************************************************************")
    print(f"\tPet Owner: {pet_owner.title()}")
    print(f"\tPet Type      : {pet_type.title()}")
