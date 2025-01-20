fruits = input("Enter a list of Fruits: ")

def print_fruits(list, idx = 0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_fruits(list, idx+1)

print_fruits(fruits)