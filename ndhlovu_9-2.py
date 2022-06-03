class Restaurant:

    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        print(f"The Name of our Restaurant is: {self.restaurant_name}")
        print(f"The Cuisine of our Restaurant is: {self.cuisine_type}\n")

    def open_restaurant(self):
        print("Restaurant is Open!")

restaurant_1 = Restaurant('Phoenix', 'African')
restaurant_1.describe_restaurant()


restaurant_2 = Restaurant('KFC', 'Fried Chiken')
restaurant_2.describe_restaurant()


restaurant_3 = Restaurant('Steers', 'Grilled Meat')
restaurant_3.describe_restaurant()
