list1 = ['a', 'b', 'c']
list2 = list()

print(list1)
print(list2)


#move elements from list1 to list2
print("\nmoving elements from list1 to list2\n")
while list1:
    temp = list1.pop()

    list2.insert(0, temp)

print(list1)
print(list2)

print("\n")

#removing all instances of an element in a list
pets = ['dog', 'dog', 'cat', 'lion', 'giraffe', 'donkey', 'cat', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)