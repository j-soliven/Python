alien_0 = {'color' : 'green', 'points' : 5 }

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# adding new key-value pairs to alien_0 dictionary
alien_0['x-position'] = 0
alien_0['y-position'] = 25
print(alien_0)

# empty dictionary
alien_1 = {}
alien_1['color'] = 'blue'
alien_1['points'] = 25
print(alien_1)

# overwriting value at key
alien_1['color'] = 'yellow'
print(alien_1)

# removing key-value pair in dictionary
del alien_1['points']
print(alien_1)

print(alien_1)