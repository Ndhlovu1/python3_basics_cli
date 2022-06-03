print("Please Enter Choose  a size: \nLarge\tMedium\tSmall")
print("The Sizes are Case Sensitive\n\n\n")

def make_shirt(size, msg):
    if size == "Small":
        print(f"\nShirt Size: \t{size}\nMessage on Shirt: \t{msg}")
    else:
        print("I love Python")

make_shirt(size = input("Enter a Size\n"),msg = input("Please Enter a Message\n"))
