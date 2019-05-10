class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name.title()
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a commmand."""
        print(self.name.title() + " rolled over!")

dog = Dog('buddy', 12)
dog.sit()
print(dog.name)