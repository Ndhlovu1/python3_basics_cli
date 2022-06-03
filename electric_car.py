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
    def __init__(self, battery_size = 75):
            self.battery_size = battery_size

    def describe_battery(self):
        """Describe battery Size"""
        print(f"This car has {self.battery_size}-kWh")

class Electric_Car(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    """A simple attempt to model for an electric"""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class"""
        #Super allows us to call methods from the parent class
        super().__init__(make, model, year)
        self.battery = Battery()

    """To Overide a parent method you need to recall that same method in the child class, hence the parent method gets overriden"""
    def fill_tank(self):
        print("This car doesnt need a tank!")

my_tesla = Electric_Car('Tesla','Model S', 2020)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_tank()
