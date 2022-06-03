sandwich_orders = ['tuna','vegeterian','bolony']
finished_sandwiches = []




while sandwich_orders:
    done_order = sandwich_orders.pop()

    print(f"I've made your {done_order} sandwich")

    finished_sandwiches.append(done_order)
print("*************************sandwiches Made*********************************")
for done_order in finished_sandwiches:
    print(done_order.title())
