class BankAccount:
    def __init__(self, balance) -> None: 
        self.int_rate = 0.01
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Your Balance is ${amount}")
    
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount + 5
            print(f" Your new Balance: ${self.balance}")
        else:
            print("Insufficient funds")

    def display_account_info(self):
        print(f" balance: {self.balance}")

    def yield_interest(self):
        if self.balance > 0:
            interst = self.balance * self.int_rate
            print(f" You earned ${interst} in interst. New balance: ${self.balance + interst}")

account1 = BankAccount(0)
account2 = BankAccount(0)

print(f"Your Balance is: ${account1.balance}")
account1.deposit(1000)
account1.deposit(300)
account1.deposit(3000)
print(f"Your New Balance is: ${account1.balance}")
account1.withdraw(4000)
print(f"Your New Balance is: ${account1.balance}")
account1.yield_interest()

print("-----------------")

print(f"Your Balance is: ${account2.balance}")
account2.deposit(100)
account2.deposit(1000)
print(f"Your New Balance is: ${account2.balance}")
account2.withdraw(1100.1)
print(f"Your New Balance is: ${account2.balance}")
account2.yield_interest()