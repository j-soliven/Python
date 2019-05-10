def build_profile(first, last, **user_info): #build a dict **
    """Build a dictionary containing everything we know about a user"""
    profile = {}
    profile['first name'] = first
    profile['last name'] = last

    for k, v in user_info.items():
        profile[k] = v

    return profile

user_profile = build_profile('j', 'soliven', location = 'USA', field = 'CS')
print(user_profile)

# importing from another module
import more_funcs

more_funcs.make_pizza('pepperoni', 'mushrooms', 'sausage')

# importing specific functions

from return_funcs import build_personV2

#build_personV2('j', 'soliven')

# as operator gives module/function an alias
import more_funcs as mf
mf.make_pizza('oregano')

# * operator in import 
# import every function in a module using asterisk operator
from more_funcs import *