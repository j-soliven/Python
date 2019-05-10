class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        full_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return full_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Method to update the odometer reading to given value."""
        if mileage < self.odometer_reading:
            print("You can't roll back an odometer!")
        else:
            self.odometer_reading = mileage
my_car = Car('audi', 'a4', 2016)
print(my_car.get_descriptive_name())
my_car.read_odometer()

my_car.update_odometer(15)
my_car.read_odometer()

# mutate the odometers reading in line
my_car.odometer_reading = 23
my_car.read_odometer()

# try to update mileag to lower value
my_car.update_odometer(12)
my_car.read_odometer()



