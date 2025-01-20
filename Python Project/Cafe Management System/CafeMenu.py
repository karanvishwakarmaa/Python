#Define the menu of restaurant....

menu = {
    "Pizza":320,
    "burger": 120,
    "Fries": 80,
    "Coke": 50,
    "Pasta": 150,
    "Cold Coffee": 150,
    "Tea": 70
}

#Greet
print("Welcome to Python Restaurant!")
print("Pizza: Rs320\nBurger: Rs120\nFries: Rs80\nCoke: Rs50\nPasta: Rs150\nCold Coffee: Rs150\nTea: Rs70\n")

order_Total = 0

#Get the user order
item1 = input("Enter the name of item you want to order =")
if item1 in menu:
    order_Total += menu[item1]
    print(f"Your item {item1} has been added to your order.")

else:
    print(f"Ordered Item (item) is not available yet!!!")

another_order = input("Do You want to add Another Item? (Yes/No) ")
if another_order == "Yes":
    item2 = input("Enter the name of item =")
    if item2 in menu:
        order_Total += menu[item2]
        print(f"Item {item2} has been added to order")

    else:
        print(f"Ordered item {item2} is not available!!!")

print(f"The total amount of item to pay is {order_Total}")