requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:    
    print("Adding extra cheese.")    
print("\nFinished making your pizza!")

# doesn't work with if-elif-else block

# if statement inside of for loop
other_toppings = ['mushrooms' , 'green peppers', 'extra cheese']
for topping in other_toppings:
    if topping == 'green peppers':
        print("Sorry we are out of green peppers")
    else:
        print("Adding " + topping)