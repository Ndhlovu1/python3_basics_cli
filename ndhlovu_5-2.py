#Conditional Test
car = 'Nissan'
print("Is car == 'Nissan'? I predict True.")
print(car == 'Nissan')

print("\nIs car == 'audi'? I predict false")
print(car == 'audi')

food = 'pizza'
print("\nIs food == 'pizza'? I predict true")
print(food == 'pizza')

car2 = 'Urus'
print("\nIs Car2 == 'Urus'? I predict true")
print(car2 == 'Urus')

print("\nIs car2 == 'audi'? I predict false")
print(car2 == 'audi')

city = 'Windhoek'
print("\nIs City == 'windhoek'? I predict True")
print(city.lower() == 'Windhoek')

print("\nIs city == 'Tokyo'? I predict false")
print(city == 'Tokyo')

print("\nIs city == 'Cape Town'? I predict false")
print(city == 'Cape Town')

country = 'Namibia'
print("\nIs Country == Namibia? I predict True")
print(country == 'Namibia')

print("\nIs Country == 'Cape Verde'? I predict false")
print(country == 'Cape Verde')

age_1 = 22
print(age_1 >= 25)
print(age_1 >21)
print(age_1 < 25)
print(age_1 <= 25)

age_2 = 16
print(age_1 < 25 or age_2 > 50)
print(age_1 < 25 and age_2 > 50)

drinks = ['Coke','Fanta','Fruitree','Pineapple']
print('chocolate' in drinks)

print('Coke' in drinks)
drink_1 = 'Orange'

if drink_1 not in drinks:
    print(f'{drink_1.upper()}, flavor not found on Drink Menu')
