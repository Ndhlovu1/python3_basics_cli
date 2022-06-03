class User:

    def __init__(self, first_name, last_name, age, gender, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.country = country

    def describe_user(self):
        print(f"Full Name: {self.first_name} {self.last_name}")
        print(f"Age      : {self.age}")
        print(f"Gender   : {self.gender}")
        print(f"Country  : {self.country}")

    def greet_user(self):
        print(f"Hi, {self.first_name} {self.last_name}\n")
        print("************************** Below Are Your Default Profile Details: *************************")

user = User('Sultan','Tin',23,"Male","Zimbabwe")
user.greet_user()
user.describe_user()

"""
user_response = input("Would you like to enter more information? (Yes/No)\n")
def enter_Details():
    if user_response.lower() == "yes":
        user = User(input("\nEnter Your Name:\n"),input("Enter Your Surname:\n"),input("Enter Your Age:\n"),input("Enter Your Gender:\n"),input("Enter your Country of Residence:\n"))
        user.greet_user()
        user.describe_user()
    else:
        exit()
enter_Details()
"""

class Priviliges:

    def __init__(self, privileges):
        privileges = ['Can Add Post','Can Delete Post', 'Can Ban Users','Can Unblock Users']
        self.privileges = privileges

    def get_privliges(self):
        print("******************************** Below Are the Admin Privileges ********************************")
        for privilege in self.privileges:
            print(privilege)

class Admin(User):

    def __init__(self,first_name, last_name, age, gender, country):
        super().__init__(first_name, last_name, age, gender, country)
        #Below was my 1 variable headache Lool
        self.privileges = Priviliges(0)

admin = Admin('Ndhlovu','Tinomudaishe',21,"Male","African")
#privileges = ['Can Add Post','Can Delete Post', 'Can Ban Users','Can Unblock Users']
admin.privileges.get_privliges()
