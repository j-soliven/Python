magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!")

#4-1 Pizzas
pizzas = ['cheese', 'sausage', 'pepperoni']

for pizza in pizzas:
    print("I like " + pizza + " pizza")
print("I really love pizza!")

#4-2 Animals
animals = ['dogs', 'cats', 'mice']

for animal in animals:
    print(animal)
print("Cool")


#------------------------------------------------------

for value in range(1,5):
    print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,13,5))
print(even_numbers)


print("printing n squares")
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

squares[0] = 25
print(squares)

for value in range(1,11):
    squares.append(value**2)
print(squares)

digits = list(range(1,11))
print(min(digits))
print(max(digits))
print(sum(digits))