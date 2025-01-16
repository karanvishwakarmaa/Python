nums = (1,4,9,16,25,36,49,64,81,100)
x = 36
i = 0 #initilization counter
while i< len(nums):
    if(nums[i] == x):
        print("Found at index", i)
        break #it will break the loop as soon as the element is found.
    else:
        print("Finding..")
    i += 1