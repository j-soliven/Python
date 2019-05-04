current_num = 1
while current_num <= 5:
    print(current_num)
    current_num += 1

#while loop to quit when user enters quit
prompt = "\nTell me something and I will repeat it back to you: "
prompt += "Enter 'quit' to exit the program. "

message = ""
while message != 'quit':   
    message = input(prompt)
    
    if message != 'quit':
        print(message)    


active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

while True:
    message = input(prompt)

    if message == 'quit':
        break
    else:
        print(message)
