#practice with if statements in for loops
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'test'
print(car.title() == car.capitalize())
#.title() and .capitalize() are same
#string equality is case sensitive, convert to lower if checking for sameness
