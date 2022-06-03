#The ** are called Kwargs and are used when the input type is unknown
def build_profile(first,last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('tino','ndhlovu',
    location='Windhoek',
    field='software',
    fav_book='Think and Grow Rich',
    fav_place = 'To be Discovered',
    age = 21
    )

print(user_profile)
