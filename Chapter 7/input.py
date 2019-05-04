message = input("Tell me someting, and I will repeat it back to you: ") #store input into message variable
print(message)

name = input("\nPlease enter your name: ")
print("Hello " + name.title() + "!\n")

prompt = "If you tell us who you are, we can personalize the messages you see." #store prompt in a variable
prompt += "\nWhat is your first name? "

name = input(prompt) #display prompt var
print("Hello, " + name.title() + "!\n")


age = input("\nWhat is your age?: ")
age = int(age)

print(age >= 18)

height = input("\nHow tall are you, in inches? ")
height = int(height)
if height >= 36:
    print("You're tall enough to ride!")
else:
    print("You'll be able to ride when you're a little older.")

