import json

numbers = [2, 3, 5, 7, 11, 13]

filename = '/home/jsoliven/github/Python/Chapter 10 - Files and Exceptions/numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)