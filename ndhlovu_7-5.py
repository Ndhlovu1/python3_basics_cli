age = "\nHow old are you?"
age += "\nEnter -1 To Quit\n"

while True:
    tkt = input(age)
    tkt = int(tkt)

    if tkt == -1:
        break

    elif tkt < 3:
        print('Free Ticket!')
        print("Enjoy your Movie!\nGoodbye!")
        break

    elif tkt < 12:
        print('Price is : $10')
        print("Enjoy your Movie!\nGoodbye!")
        break

    elif tkt > 12 :
        print('Price is : $15')
        print("Enjoy your Movie!\nGoodbye!")
        break
