#Define a Class
class Dog:

    """
    Modelling a Dog,(Our real life situation)
    """
#Create a docstring defining what the class does
#The __init__ method is run each time an instance is created from class dog
#The two trailing underscores differentiate my classes from clashing with pythons default methods
#Each and every Method call associated with an instance in python must pass the self argument before everything else, and it is always automatically sent by python when a method call occurs

    def __init__(self, name, age):
        """Initialize name and age Attributes"""
#Any variable prefixed with self is available to all methods in the class
#The variables below are called attributes as the assign their values to either name/age whenever an instance is created
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """SImulate rolling over"""
        print(f"{self.name} is rolling roll_over")

my_dog = Dog(input("Enter Dog Name\n"),12)
print(f"My dog's name is {my_dog.name}.")
print(f"{my_dog.name} is {my_dog.age} years old")
my_dog.sit()

your_dog = Dog('Keni',3)
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog's age is {your_dog.age} years old")
#Calling the methods of Dog, using the . notation
your_dog.sit()
