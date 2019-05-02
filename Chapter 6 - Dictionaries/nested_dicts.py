alien = []

for i in range(30):
    new_alien = { 'color' : 'green', 'points': 5, 'speed' : 'slow'}
    alien.append(new_alien)

for alien in alien[:5]:
    print(alien)