sandwich_orders = ['tuna','vegeterian','bolony','pastremi','pastremi','pastremi']
finished_sandwiches = []

while 'pastremi' in sandwich_orders:
    print("The Deli has run out of Pastrami.")


while sandwich_orders:
    done_order = sandwich_orders.pop()

    print(f"I've made your {done_order} sandwich")

    finished_sandwiches.append(done_order)
print("*************************sandwiches Made*********************************")
for done_order in finished_sandwiches:
    print(done_order.title())
