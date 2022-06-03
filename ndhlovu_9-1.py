class Restaurant:

    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        print(f"The Name of our Restaurant is: {self.restaurant_name}")
        print(f"The Cuisine of our Restaurant is: {self.cuisine_type}")

    def open_restaurant(self):
        print("Restaurant is Open!")

restaurant = Restaurant('Phoenix', 'African')
restaurant.describe_restaurant()
restaurant.open_restaurant()
