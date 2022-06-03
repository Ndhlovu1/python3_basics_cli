#Adding Data to a dictionary

dream_vacation = {}

#Set a flag that polling is active
polling_active = True

while polling_active:
    #Prompt for person's Name
    name = input("\nWhat is your name?\n")
    mountain = input("\nWhere would you like to go?\n")
    dream_vacation[name] = mountain

    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == 'no':
        polling_active = False

#Polling is complete. Show the results
print("\n-------------------------------Polling Results-----------------------")
for name,variable in dream_vacation.items():
    print(f"{name} would like to visit {mountain}")
