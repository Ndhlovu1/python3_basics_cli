def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\n(Press 'q' to Quit)\n")
    print("\nPlease tell me your name:\n")

    f_name = input("\nFirst Name:\n")
    if f_name == 'q':
        break

    l_name = input("\nLast  Name:\n")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name,l_name)
    print(f"\nHello, {formatted_name}!")
