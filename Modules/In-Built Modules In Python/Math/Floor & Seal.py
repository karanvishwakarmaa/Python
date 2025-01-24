import math

a = float(input("Enter the number for find Floor & Ceil Number's: "))
print("""Choice What You Want Floor Or Ciel...
1. For Floor Numbers Modules...
2. For Ceil Numbers Modules...
""")

choice = int(input("Enter Your Choice (1 or 2): "))
if choice == 1:
    k = math.floor(a)
    print("Your Number Of Floor Module is: ", k)
if choice == 2:
    r = math.ceil(a)
    print("Your Number Of Ceil Module is: ", r)

