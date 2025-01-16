numbers = (1,4,9,16,25,36,49,64,81,100, 1,4,9,16,25,36,49,64,81,100)

x = int(input("Enter Your Any Number: "))
idx = 0
for num in numbers:
    if(num == x):
        print("Number found at indx", idx)
        break
    idx += 1