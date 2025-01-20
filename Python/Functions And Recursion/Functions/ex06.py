num = int(input("Enter number: "))

def OddEven(nums):
    if(nums % 2 == 0):
        print("This is Even Number and Your number is =", nums)
    else:
        print("This is Odd Number and Your number is =", nums)
    
OddEven(num)