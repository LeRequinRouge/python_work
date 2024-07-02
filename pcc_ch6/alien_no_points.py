# program to intentionally cause an error
# by trying to access a value that doesn't exist
alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])

# if points exist, the value is used...
# otherwise the default value is used
# which in this case is 'No point val...'
# if the second argument is blank python returns 'None'
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)