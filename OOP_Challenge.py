class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Funds Unavailable!")
        else:
            self.balance -= amount
            print("Withdrawal Accepted")

    def deposit(self, amount):
        self.balance += amount
        print("Withdrawal Accepted")


acct1 = Account('Jose',100)
print(acct1.balance)

acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)