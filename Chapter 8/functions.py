def greetuser():
    """Displays a simple greeting."""
    print("Hello!")

greetuser() #rfunction call


#passing arguments to a function

def greet_user(username):
    """Displays a simple greeting to the given name"""
    print("Hello " + username.title())

greet_user("john")