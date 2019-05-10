def print_models(unprinted, completed):
    """Simulate printing each design, until non e are left.
    Move each design to completed after printing."""
    while unprinted:
        current_design = unprinted.pop()
        print("Printing model: " + current_design)
        completed.append(current_design)

def show_completed(completed):
    print("\nThe following models have been printed: ")
    for x in completed:
        print(x)

unprinted = ['iphone case', 'robot pendant', 'dodecahedron']
completed = []


# print_models(unprinted, completed)
# send a copy of the list to the function
print_models(unprinted[:], completed)
show_completed(completed)
print(unprinted)


# passing arbitrary number of arguments
# the param with arbitrary number of arguments comes last

def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print(" - " + topping)

make_pizza('pepperoni')
make_pizza('cheese', 'mushrooms', 'pepperoni', 'onions')
