alien_0 = {'x_position':0,'y_position':0,'speed':'medium'}
print(f"Original Position:  {alien_0['x_position']}")

#Move the alien to the right
#Determine how far to move the Alien
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

#The new position is the Old Position + the New Position
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New Position: {alien_0['x_position']}")
#To remove a nolonger useful value from a dictionary use the del statement, all it needs is the Key
#the Deleted Value is permanently gone
del alien_0['y_position']
print(alien_0)
