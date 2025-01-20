name = input("Enter Your Name: ")
marks = []
English = int(input("Enter 1st Subject Marks: "))
Hindi = int(input("Enter 2nd Subject Marks: "))
Math = int(input("Enter 3rd Subject Marks: "))
Physics = int(input("Enter 4nd Subject Marks: "))
Chemistry = int(input("Enter 5rd Subject Marks: "))

marks.append(English)
marks.append(Hindi)
marks.append(Math)
marks.append(Physics)
marks.append(Chemistry)

class Student:
    def __init__(self, name, marks): 
        self.name = name
        self.marks = marks
        


    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
            print("Hi!\n", self.name, "Your avg Score is: ", sum/5)
s1 = Student(name, marks)
s1.get_avg()
# print(s1)