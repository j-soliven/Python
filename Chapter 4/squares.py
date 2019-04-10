squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)

# better way

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

digits = list(range(1,10))
digits.append(0)
print(digits)

print(min(digits))
print(max(digits))
print(sum(digits))


