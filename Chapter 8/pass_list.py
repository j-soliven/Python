# passing a list to a function 
import functions

def greet_users(names):
    for name in names:
        print("Hello " + name.title() + "!")

greet_users(['john', 'francesca', 'josh'])


before = [1, 2, 3, 4, 5]
after = []

for x in before:
    after.append(before.pop())

after.sort()
print(after)