#recursive Function
n = int(input("Enter Any Number for recursive Mode: "))

def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
show(n)