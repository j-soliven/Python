players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

print(players[:4]) #works with no starting index
print(players[2:]) #works with no ending index
print(players[-3:]) #prints last three

for player in players[:3]:
    print(player.title())