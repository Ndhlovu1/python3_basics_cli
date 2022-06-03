class Car:

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
#Some attributes can be created and assigned a default value outside of the init ()
        self.odometer_reading = 0


    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.model} {self.make}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the cars """
        print(f"This car has {self.odometer_reading} miles on it")
#Updating an instance directly via a method
    def update_odometer(self, mileage):
        #Set a reading
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cant roll back an Odometer")

    def increment_odometer(self, miles):
#Add given amount to odometer reading
        self.odometer_reading += miles


class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This has a {self.battery_size}-kWh battery")

    def get_range(self):
        #Distance
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This Car can go about {range} miles on a full charge")



class ElectricCar(Car):

    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery(75)

my_tesla = ElectricCar('tesla','model s', 2020)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

"""
my_new_car = Car("Urus", 'Auto', 2020)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()
"""
