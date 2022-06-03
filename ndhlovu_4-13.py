print("                     Buffet")
print("")

print("Welcome to the 2021 Buffet Menu")
menu = ('Pizza','Hotdogs','Sausages','Mac n Cheese')

for menu_Item in menu:
    print(menu_Item)

#The Error
#menu[0] = 'Error'
menu = ('Pizza','Hotdogs',"Spaghetti","Rice")
print("Below is the New Menu")
for menu_Item2 in menu:
    print(menu_Item2)
