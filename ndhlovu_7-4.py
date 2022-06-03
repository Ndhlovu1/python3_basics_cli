pizza_topping = "\nPlease Choose a topping"
pizza_topping += "\nEnter quit When Finished\n"


while True:
    top = input(pizza_topping)

    if top == 'quit':
        break
    else:
        print(f"We'll add {top} to your pizza")
