class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance
    def deposit(self, amount):
        if amount < 0:
            print("You can only deposit an amount greater than zero")
        else:
            self.account_balance += amount
            return f"Deposited: ${amount:.2f}"
    def withdrawal(self, amount):
        if self.account_balance > amount :
            self.account_balance -= amount
            return True
        else :
            return False 
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")