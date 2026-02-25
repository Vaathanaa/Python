class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        print(f"Depositing ${amount}")
        self.balance += amount
        print(f"New balance: ${self.balance}")

    def withdraw(self, amount):
        print(f"Withdrawing ${amount}")
        if amount <= self.balance:
            self.balance -= amount
            print(f"New balance: ${self.balance}")
        else:
            print(f"Attempting to withdraw ${amount}")
            print("Insufficient funds. Withdrawal failed.")
account = BankAccount("Vathana", 1000)
account.deposit(500)
account.withdraw(300)
account.withdraw(2000)
        
        