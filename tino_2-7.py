"""
This Program takes in a Name Variable then begins to edit the data before it is used by our Program.
Takes a Variable then begins to remove either trailing/preceding white spaces that a user would've entered
"""

name = " Mr. t ndhlovu "

name.lstrip()
print(f"{name}\n\tI have lost the space to my right/your left")
name.rstrip()
print({f"{name}\n\tI have lost the white space to my right")
name.strip()
print(f"{name}\n\tI have lost all the white spaces")
