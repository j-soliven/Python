responses = {}

active = True

while active:
    name = input("Enter your name: ")
    response = input("What is your favorite color? ")

    responses[name] = response

    repeat = input("Enter yes to add another person or no to stop polling: ")
    if repeat == 'no':
        active = False

print("\n---RESULTS---")
for name, response in responses.items():
    print(name.title() + ": " + response)       