class User:

    def __init__(self, first_name, last_name, age, gender, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.country = country
        self.login_attempts = 0

    def increment_login_attempts(self, increase):
        #increase = 1
        if increase >= self.login_attempts:
            self.login_attempts += 1
            print(f"{self.login_attempts} login attempts")

        #self.login_attempts += increase
        #print(f"{self.login_attempts} Login Attepts Left.")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.login_attempts,': login attempts reset')


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
user.increment_login_attempts(0)
user.increment_login_attempts(1)
user.increment_login_attempts(1)
user.increment_login_attempts(2)
user.increment_login_attempts(5)
user.reset_login_attempts()

user_response = input("\nWould you like to enter more information? (Yes/No)\n")
def enter_Details():
    if user_response.lower() == "yes":
        user = User(input("\nEnter Your Name:\n"),input("Enter Your Surname:\n"),input("Enter Your Age:\n"),input("Enter Your Gender:\n"),input("Enter your Country of Residence:\n"))
        user.greet_user()
        user.describe_user()
    else:
        exit()
enter_Details()
