"""

Things to be stored into:
    Cities
    Countries
    Food
"""

print("**************************************************************************************************")
print("\tThe List of Places I would like to visit")
print("*                                                                                                *")


cities = ['Kigali','Moscow','Beijing','Sentosa']

print("\nWe are going to view the List of Cities I'd like to visit if am to visit alphabetically .. :)")
temp_srtd = sorted(cities)
print(temp_srtd)

print("**************************************************************************************************")
print("\tThe List of Places I would like to visit if i am to just wake up and leave the house :) ")
print("*                                                                                                *\n")
print(cities)

print("**************************************************************************************************")
print("\tThe List of Delicacy I would prefer to Enjoy while Visiting these places ")
print("*                                                                                                *")

food = ['Big Fish','African-Sushi','Sushi','Bamboo Rice']
print("\nWe are going to view the List of food in Sorted.. :)")
sorted(food)
print(food)

print("\nWe are going to view the List of food now in counter Sorted ... :)")
print(sorted(food, reverse= True))

print("**************************************************************************************************")
print("\tThe List of Countries I would prefer to Enjoy while Alive ")
print("*                                                                                                *")
countries = ['China', 'Singapore','Rwanda','Russia']
print("\nBelow is the Original View of the Countries\n",countries)
countries.sort()
print('Here is a sorted list of all the countries I would like to visit\n', countries)
countries.reverse()
print('Below is a sorted list placed in Reverse\n', countries)

print("####################################################################################################")
print('Below is the List of the Country, City and Delicacy combined.')
countries = ['China', 'Singapore','Rwanda','Russia']
print(countries[0],',',food[-1],',',cities[2])
print(countries[1],',',food[2],',',cities[-1])
print(countries[2],',',food[1],',',cities[0])
print(countries[3],',',food[3],',',cities[1])
