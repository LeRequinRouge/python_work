alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

# list containing dictionaries
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# making a fleet of aliens more efficiently
aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# change the first 3 aliens
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print('...')

# shows the total number of aliens
print(f"Total number of aliens: {len(aliens)}")