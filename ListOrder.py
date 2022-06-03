#Creating Order in the type of Lists
"""
The sort() is permanant
the sorted() is temporary
    to reverse:
    e.g. cars.sort(reverse=True)
    or
    print(sorted(cars)) will sort the data out

"""
cars = ['bmw','merc','yaris']
cars.sort()
print("These cars are alphabetically sorted ", cars )

"""
Reverse:
    Simply rewrites sentence from the end to the start
    e.g. cars.reverse()
         print(cars)
"""

cars.reverse()
print(cars)

"""
Finding the Length of the List:
    cars = ['bmw','merc','yaris']
    len(cars)
"""

length = len(cars)

print(" Length is : ", length, " items")
