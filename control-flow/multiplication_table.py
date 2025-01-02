number = input("Enter a number to see its multiplication table: ")
X = int(number)
for Y in range(1,11) :
    Z = X * Y
    print(f"{X} x {Y} = {Z}")
print()