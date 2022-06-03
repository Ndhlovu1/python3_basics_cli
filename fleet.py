#Make an empty list for storing aliens
aliens=[]

#Make 30 green aliens
for alien in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

#Show thw 1st 5 Aliens
for alien in aliens[:5]:
    print(alien)
    print('...')

#Show total Aliens Created
print(f"{len(aliens)} : have been created")
