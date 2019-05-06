def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

print(get_formatted_name('j', 'soliven'))

me = get_formatted_name('j', 'soliven')
print(me)

# make an argument optional
# optional must be at end of parameters

def get_formatted_name2(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

me2 = get_formatted_name2('j', 'soliven', 'c')
me3 = get_formatted_name2('j', 'soliven')

print(me2)
print(me3)
print('\n')

# returning a dict from a function

def build_person(first_name, last_name):
    """Return a dictionary of information about a person"""
    person = {'first' : first_name, 'last' : last_name}
    return person

me = build_person('j', 'soliven')
print(me)

# making age an optional param

def build_personV2(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first' : first_name, 'last' : last_name}
    if age:
        person['age'] = int(age)
    return person

me = build_personV2('j', 'soliven', 19)
print(me)

test = ''

while test != 'quit':
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print('\n' + formatted_name)

    test = input("\nType 'quit' to quit program")


