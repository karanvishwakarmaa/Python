def check_Word():
    word = "learning"
    with open("practice.txt", "r") as f:
        data = f.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("Not Found")

check_Word()

def Check_Line():
    word = "learning"
    data = True
    line_no = 1
    with open ("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    
    return -1

Check_Line()