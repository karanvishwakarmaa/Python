class Account:
    def __init__(self, balance, account):
        self.balance = balance
        self.account = account

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited Successfully...")
        print("Total Balance =", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was Credited Successfully...")
        print("Total Balance =", self.get_balance())

    def get_balance(self):
        return self.balance
    

account1 = Account(10000, 123456789)
account1.debit(1000)
account1.credit(100)