#continue statement loops back to beginning of loop without executing rest of code

num = 0

while num < 10:
    num += 1
    if num % 2 == 0:
        continue

    print(num)