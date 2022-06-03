
fav_pizza = ['Hawai','Mexican','Meaty Cheese','Potato Soup', 'Sadza', 'Kapana']

#Loop to tell type of pizza i like
for pizza in fav_pizza[:3]:
    print("The first 3 Items Are: \n")
    print(pizza)
print('Full List: ', fav_pizza)

#Loop through from the Middle
for mid_pizza in fav_pizza[3:]:
    print(mid_pizza)
print("The Above printed from the beginning.")
print(fav_pizza)

for lst_pizza in fav_pizza[-3:]:
    print(lst_pizza)
