def greetuser():
    """Displays a simple greeting."""
    print("Hello!")

greetuser() #rfunction call


#passing arguments to a function

def greet_user(username):
    """Displays a simple greeting to the given name"""
    print("Hello " + username.title())

greet_user("john")

# keyword arguments
# position does not matter

def describe_pet(pet_name, animal_type):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name)

describe_pet(pet_name = 'Sparky', animal_type = 'dog')
describe_pet(animal_type = 'dog', pet_name = 'Sparky')


# default value functions
def describe_pet2(petname, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + petname.title() + ".")

describe_pet2('sparky')
describe_pet2('sparky', 'cat')