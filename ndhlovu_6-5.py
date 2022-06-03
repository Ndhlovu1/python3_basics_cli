rivers = {
    'nile':'egypt',
    'lake tanganyika':'tanzania',
    'zambezi':'zimbabwe'
    }

for river,country in rivers.items():
    print()
    print(f"The {river.title()} river runs through {country.title()}")

print("****************All Rivers **************************")
for river,country in rivers.items():
    print(f"{river.title()} river that's in the Dictionary:\n")

print("****************All Countries **************************")
for river,country in rivers.items():
    print(f"{country.title()} river that's in the Dictionary:\n")
