class User:

    def __init__(self, first_name, last_name, age, gender, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = int(age)
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
