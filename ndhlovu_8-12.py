def sandwich(*items):
    print("Below is a list of Item(s) to be added to Sandwich")
    for fd_item in items:
        print(f"-{fd_item}\n")

sandwich_items = ['Peanut Butter','Magarine','Onions','Tomatoes','Spinach']
sandwich_items2 = ['Cabbage','Storch','Eggs']
sandwich_items3= ['Bacon']
sandwich(sandwich_items3)
sandwich(sandwich_items2)
sandwich(sandwich_items)
