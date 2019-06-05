import json

username = input("What is your name?: ")

filename = 'Chapter 10 - Files and Exceptions/username.json'

with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remmeber you when you come back, " + username + "!")