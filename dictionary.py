"""
Dictionaries allow the storage of any information that can be matched up

e.g. person = {'Country':'Namibia', 'Age':20}
print(person['Country'])
print(person['Points'])


A dictionary is a collection ok Key-Value Pairs, you access the value through the key associated with that value
The Value can be a Number, String, List, or even another dictionary.

Every Key is connected to it's Value by a Colon, while individual key-value pairs are seperated by a Comma,

"""

person = {'Citizenry':'Namibian', 'Age':20}
#print(person['Country'], person['Age'])
#print(person['Age'])

#Adding Information to a dictionary
person['City'] = 'Luderiz'
person['Race'] = 'Black'
print(person)

print()
print("Below is a New dictionary")
#We are going to start with an Empty dictionary
usr = {}
id = 1
usr['Name'] = 'Phoenix'
usr['Surname'] = 'Sultan'
usr['Email'] = 'sultan@gmail.com'
usr['Password'] = '1234+'
usr['Id'] = id
print(usr)

print()
print()
print("You can also store similar information within a dictionary")
#e.g
print("Polling Data:")
fav_lang = {
    'jen':'python',
    'Julia':'C',
    'Ken':'Java',
    'jeni':'C++',
}
print(fav_lang)
#You can Use the get(key,value) method if a requested key doesnt exists
point_value = {'name','No value Assigned'}
