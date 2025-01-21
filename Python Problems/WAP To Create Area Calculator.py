print("*****Area Calculator*****")

print("""Press 1 to get the Area of Square
Press 2 to get the Area of Rectangle
Press 3 to get the Area of Circle
Press 4 to get the Area of Triangle
""")

choice = int(input("Enter a Number B/w 1-4: "))
if choice == 1:
    side = float(input("Enter the length of one side: "))
    area = side**2
    print("The Area of Square is", area)

elif choice == 2:
    length = float(input("Enter the length of Rectangle: "))
    width = float(input("Enter the width of Rectangle: "))
    area = length*width
    print("The Area of rectangle is", area)

elif choice == 3:
    radius = float(input("Enter the radius of Circle: "))
    area = ((22/7)*(radius**2))
    print("The Area of the Circle is", area)


elif choice == 3:
    base = float(input("Enter the base of traingle: "))
    height = float(input("Enter the height of triangle: "))
    area = 0.5*base*height
    print("The Area of the Circle is", area)

else:
    print("Invalid Input...")

