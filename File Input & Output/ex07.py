data = input("Enter Your 6 times data :")
count = 0
def ByUser():
    with open("practice.txt", "w") as f:
        d = f.write(data)
    # print(data)
    # print(type(d))
    
    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

    # num = ""
    # for i in range(len(data)):
    #     if data[i] == ",":
    #         print(int(num))
    #         num = ""
    #     else:
    #         num += data[i]

# ByUser()
print(count)