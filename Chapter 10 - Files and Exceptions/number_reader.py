import json

filename = '/home/jsoliven/github/Python/Chapter 10 - Files and Exceptions/numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)