"""
#This program opens/reads from a file
#To work with any file, u must open the file first
#The open() needs a single argument, the name of the file u want to open
#Python looks for this file in the directory where the code is running from
#open('pi_digits') returns an object representing pi_digits, it's assigned to file_object
#Keyword with closes the file once it's no longer needed.
#The open() tells python to figure out when to close the file
#We then use the .read() to read the entire contents of the file
"""
file_path = '/Home/Desktop/pyth/read/text_files/pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()

print(contents.rstrip())
