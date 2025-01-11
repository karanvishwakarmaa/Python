name = input("Enter Your Name :")
age = int(input("Enter Your Age :"))
teaching = input("Enter Your Class...")

if(teaching == "10" or teaching == "10th"):
    print("10th Class Section")
    engl = int(input("Enter Your English Marks :"))
    hindi = int(input("Enter Your Hindi Marks :"))
    sanskirt = int(input("Enter Your Sanskrit Marks :"))
    social = int(input("Enter Your Social Marks :"))
    science = int(input("Enter Your Science Marks :"))
    math = int(input("Enter Your Math Marks :"))

    total = (engl+hindi+sanskirt+social+science+math)/6

    if(total >= 90):
        print("You r doing Great, You Have 'A' Grade", total)
    elif(total >= 80 and total < 90):
        print("You r doing Great, You Have 'B' Grade", total)
    elif(total >= 70 and total < 80):
        print("You r doing Great, You Have 'C' Grade", total)
    elif(total >= 60 and total < 70):
        print("You r doing Great, You Have 'D' Grade", total)
    else:
        print("You Are Fail ...", total)

else:
     print("12th Class Section")
engl = int(input("Enter Your English Marks :"))
hindi = int(input("Enter Your Hindi Marks :"))
social = int(input("Enter Your Physics Marks :"))
science = int(input("Enter Your chemistry Marks :"))
math = int(input("Enter Your Math Marks :"))

total = (engl+hindi+social+science+math)/5

if(total >= 90):
        print("You r doing Great, You Have 'A' Grade", total)
elif(total >= 80 and total < 90):
        print("You r doing Great, You Have 'B' Grade", total)
elif(total >= 70 and total < 80):
        print("You r doing Great, You Have 'C' Grade", total)
elif(total >= 60 and total < 70):
        print("You r doing Great, You Have 'D' Grade", total)
else:
        print("You Are Fail ...", total)