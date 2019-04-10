bicycles = ['trek', 'cannondale', 'redline', 'specialzed']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())

print(bicycles[-1])
print(len(bicycles))
print(bicycles[(len(bicycles) - 1)])

print('\n\n')

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

#3-1 Names
friends = ['john', 'jack', 'michael','matt']

for x in friends:
    print(x)

#3-2 Greetings
print("Hello " + bicycles[0])

for x in friends:
    print("hello " + x)
