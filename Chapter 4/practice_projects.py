#4-3
for value in range(1,21):
    print(value)

#4-4

#for value in range(1,1000001):
#    print(value)

#4-5
million = list(range(1,1000001))
print(min(million))
print(max(million))
print(sum(million))


#4-6 Odd Numbers
odd = [value for value in range(1,21,2)]
for value in odd:
    print(value)

#4-7 Threes
threes = [value for value in range(0,31,3)]
for value in threes:
    print(value)

#4-8 Cubes && Cube Comprehension
cubes = [value**3 for value in range(1,11)]
for x in cubes:
    print(x)

