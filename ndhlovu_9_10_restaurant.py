class Restaurant:

    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def get_customers_served(self):
        print(f"{self.number_served} Customers have been served.")

    def set_number_served(self, served_customers):
        self.number_served = served_customers

    def describe_restaurant(self):
        print(f"The Name of our Restaurant is: {self.restaurant_name}")
        print(f"The Cuisine of our Restaurant is: {self.cuisine_type}")

    def open_restaurant(self):
        print("Restaurant is Open!")
"""
restaurant = Restaurant('Phoenix', 'African')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(20)
restaurant.get_customers_served()
"""
class IceCreamStand(Restaurant):

    def __init__(self,restaurant_name, cuisine_type):

        super().__init__(restaurant_name, cuisine_type)
        flavours = ['Chocolate','Caramel','Toffy']
        self.flavours = flavours

    def display_flavours(self):
        for flavor in self.flavours:
            print(flavor)


iceCreamStand = IceCreamStand('Sweet Flakes', 'Deserts')
#iceCreamStand.display_flavours()
