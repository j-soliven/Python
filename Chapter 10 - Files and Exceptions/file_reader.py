with open('Chapter 10 - Files and Exceptions/pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

# with closes the file after used
# open opens the file at given file path
# file_object.read() method reads in the text from the file
print('\n\n')
filename = 'Chapter 10 - Files and Exceptions/pi_digits.txt'

with open(filename) as file_obj:
    lines = file_obj.readlines() # list of lines from file object

for line in lines:
    print(line.rstrip())

