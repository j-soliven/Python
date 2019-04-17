age = 17
#if-else statements
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18")

#if-elif-else chain
age = input("Enter age: ")
if age < 4:
    print("Admission is free")
elif 4 <= age <= 18:
    print("Admission is $5")
elif age >= 18:
    print("Admission is $10")