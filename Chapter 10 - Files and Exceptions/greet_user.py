import json


filename = 'Chapter 10 - Files and Exceptions/username.json'

with open(filename) as f_obj:
    username = json.load(f_obj) ## only need file object for json.load() method
    
print("Welcome back, " + username + "!")