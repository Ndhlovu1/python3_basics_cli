
from User_module import User

class Admin(User):

	def __init__(self, first_name, last_name, age, city, country, phone_number):
		super().__init__(first_name, last_name, age, city, country, phone_number)
		self.privileges = ["can add post", "can delete post", "can ban user"]
		self.number_of_privileges = 1 #len(self.privileges)
		#self.last_index_range = self.number_of_privileges + 1

		#self.number_of_times = range(1, self.last_index_range)

	def show_privileges(self,):
		print('User privileges:')
		for previlege in self.privileges:
			print(f'\t{self.number_of_privileges}. {previlege}')
			self.number_of_privileges +=1
