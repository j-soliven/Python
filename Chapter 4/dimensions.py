#Practice with tuples
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#change items
#dimensions[0] = 250
#cannot change element in a tuple

#need to redefine tuple to write over it
print("Original dimensions: ")
for x in dimensions:
    print(x)

dimensions = (400, 100)
print("\nModified dimensions:")
for x in dimensions:
    print(x)

ex_tuple = (1, 5, 7, 9, 12)
print(ex_tuple)
for x in ex_tuple:
    print(x)
