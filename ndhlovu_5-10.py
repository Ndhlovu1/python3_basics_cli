current_users = ['Tino','phx','Admin','racheal','topi']

new_users = ['Pena','Admin','Tino','test','taki']

for user in new_users:
    if user in current_users:
        print(f'{user.title()}, You need a new username')
    else:
        print(f'{user.title()}, Username Available')
