from ndhlovu_9_12_user import User


class Admin(User):

    def __init__(self,first_name, last_name, age, gender, country):
        super().__init__(first_name, last_name, age, gender, country)

        self.privileges = ['Can Add Post','Can Delete Post', 'Can Ban Users','Can Unblock Users']
        self.privilege = 0

    def get_privliges(self):
        print("******************************** Below Are the Admin Privileges ********************************")
        for privilege in self.privileges:
            print(privilege)
