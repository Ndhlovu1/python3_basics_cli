"""
Lists:
    Always Plural
    Seperated by Commas
    [] indicate a list
    e.g. bycicles = ['Black Momba', 22, 'Phoenix']
         print(bycicles)
    Data doesnt need to be related
"""
bycicles = ['Black Momba', 22, 'Phoenix']
print(bycicles)

"""
Lists: Accessing
        Lists work like arrays, hence they start at index 0
        e.g. print(bycicles[0])
        To Access the last item on the List
        e.g. print(bycicles[-1])
"""
print(bycicles[0])
print(bycicles[-1], "Ig")

names = ['Phoenix','Sultan','Oscar', 'Hola', 'Thiago']
print(names[0],names[1],names[2],names[3],names[4])
print("Happy 2020.1 ",names[0])
print("Happy 2020.1 ",names[1])
print("Happy 2020.1 ",names[2])
print("Happy 2020.1 ",names[3])
print("Happy 2020.1 ",names[4])

vehicles = ['BMW','Ferari','Benz']
print("I would love to own a ", vehicles[0]," motorbike")

print("I would love to own a ", vehicles[1]," motorbike")

print("I would love to own a ", vehicles[2]," motorbike")

"""
Lists: Modifying Data
        Enter the list name and the Index Position
        e.g. vehicles[0] = "Porsche"
"""

vehicles[0] = "Porsche"
print(vehicles)

"""
List: Adding Data to the List
    e.g. vehicles.append("Yamaha")
    The append() is ideal for building Lists dynamically
"""
vehicles.append("Yamaha")
print(vehicles)

"""
Lists: Inserting Data to any position in the List
        insert() creates an open space and moves every other option 1 place to the right
        e.g. vehicles.insert(index position, "Replacement Value")
"""

vehicles.insert(0, "Phoenix")
print(vehicles)

"""
Lists: Removing the Items in a List
        del list_name[] can be used to delete the data if u know it's index position
        e.g del vehicles[0] Wud delete the value of the first position
"""

del vehicles[0]
print(vehicles)

"""
Lists: pop() removing a value but still being able to use it,
        e.g. Removing a User from being Active to being Inactive, it also removes the last item in the list
        e.g. vehicles.pop()
        To remove the list, u can also use the direct index
"""
vehicles.pop()
print(vehicles)

f_bike = vehicles.pop(0)
print(f"{f_bike} is the first motorbike i plan to buy")

"""
Lists: remove() Entering a value so that it can be removed from the list
        e.g. vehicles.remove('Porsche') will tell python to search and delete Porsche from the list
"""

chopers = ['toyota','yaris','bently']
bb = chopers.remove("bently")
print(chopers)
