programming_words = {
    'Dictionary':'A way of collecting dynamic key-value information',
    'Lists':'A way of storing any types of data within a single variable',
    'Access Values':'Refers to the way of accessing the Data within a dictionary',
    'Tuple':'An information storage method built to have static data',
    'Del':'Used for permanently removing data from the computer',
    'Set':'A collection in which items must be unique',
    'Sorted','Used to adjust contents of a list/dictionary into alphabetical order'
}

#print(f"{programming_words, skip}")

#dicts = [{v:k} for k, v in programming_words.items()]
#print(dicts,'\n')

for val,ky in programming_words.items():
    print()
    print(val,ky)
