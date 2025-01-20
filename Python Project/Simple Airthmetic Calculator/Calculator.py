Operator = input("Enter an Operator (+ - * /): ")

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if Operator == '+':
        result = num1 + num2
        print(result)
elif Operator == '-':
        result = num1 - num2
        print(result)
elif Operator == '*':
        result = num1 * num2
        print(result)
elif Operator == '/':
        result = num1 / num2
        print(result)
else:
        print(f"{Operator} is not valid...")
# Operator(num1, num2)