name = input("Enter Your Name: ")
classname = input("Enter Your Class Name: ")

if(classname == "10", "10th", "Tenth"):
    english = int(input("Enter Your english marks: "))
    hindi = int(input("Enter Your hindi marks: "))
    math = int(input("Enter Your math marks: "))
    science = int(input("Enter Your science marks: "))
    socialscience = int(input("Enter Your socialscience marks: "))
    sanskrit = int(input("Enter Your sanskrit marks: "))

    total = float((english + hindi + math+socialscience+sanskrit+science)*100/600)
    
    if(total >= 90):
        print(name,"You Have Passed With /A/ Grade")
    elif(total >= 80):
        print(name,"You have passed with B Grade")
    elif(total >= 70):
        print(name,"Your have passed with C Grade")
    else:
        print(name,"You are fail")

elif(classname == "12", "12th", "twelth", "Twelth"):
    english = int(input("Enter Your english marks: "))
    hindi = int(input("Enter Your hindi marks: "))
    math = int(input("Enter Your math marks: "))
    science = int(input("Enter Your science marks: "))
    socialscience = int(input("Enter Your socialscience marks: "))


    total = {(english + hindi + math+socialscience+science)*100}/500
    
    if(total >= 90):
        print(name,"You Have Passed With /A/ Grade")
    elif(total >= 80):
        print(name,"You have passed with B Grade")
    elif(total >= 70):
        print(name,"Your have passed with C Grade")
    else:
        print(name,"You are fail")

else:
    print(name,"You are super senior")