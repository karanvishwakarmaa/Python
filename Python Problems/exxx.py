class BankAccount:
    def __init__(self, account_holder,balance):
        self.account_holder= account_holder #public attributes
        self.__balance = balance #private attribute

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"Depositeed {amount}.New Balance: {self.__balance}")
        else:
            print("Deposit Amount Must Be Positive...")

    def withdraw(self, amount):
        if 0<amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdraw {amount}.New Balance: {self.__balance}")
        else:
            print("Insufficient Funds in your account")

    def get_balance(self):
        return self.__balance #providing controlled access to private variables.

#creating an object
account = BankAccount(input("Enter Your Name: "), float(input("Enter Your Amount For Account Opening...")))

#Accessing data using methods
account.deposit(float(input("Enter Your Deposit Amount: ")))
account.withdraw(float(input("Enter Your Withdrawl Amount: ")))

print("Current Balance is: ",account.get_balance())