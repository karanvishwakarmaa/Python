class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 0

    def deposit(self, amount):
        self.deposit += amount
        print("Deposited {amount} to your acount..")

        def withdraw(self, amount):
            if amount <= self.balance:
                self.balance -= amount
                print("Withdrawl {amount} from your account..")
            else:
                print("Insufficient Funds!!!!")

                def check_balance(self):
                    print("Your Current Balance is {self.balance}")

# print(Account)