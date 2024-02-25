#Finding Right Angled in a more efficient manner
x = int(input("Enter the first side:"))
y = int(input("Enter the second side:"))
z = int(input("Enter the third side:"))

sides = sorted([x,y,z]) #sorting the sides by putting them into an array
if sides[2] ** 2 == sides[0] ** 2 + sides[1] ** 2:
    print("Right Angled Triangle")
else:
    print("Not Right Angled Triangle")