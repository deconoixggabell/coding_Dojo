class BankAccount:
    def __init__(self,int_rate, balance) -> None: 
        self.int_rate = int_rate
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

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        new_var = self.account = amount
        new_var += amount

    def withdraw(self, amount):
        if amount < self.account:
            self.account -= amount + 5
        else:
            print("Insufficient funds")

user1 = User("Mark","mark@email.com")
user1.make_deposit(100)
print(f"User:{user1.name} Balance ${user1.account}")
user1.withdraw(10)
print(f"User:{user1.name} New Balance ${user1.account}")

user2 = User("Jim", "jim@email.com")
user2.make_deposit(1000)
print(f"User:{user2.name} Balance ${user2.account}")
user2.withdraw(200)
print(f"User:{user2.name} New Balance ${user2.account}")


''''SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to

SENPAI BONUS: Add a transfer_money(self, amount, other_user) method to the user class that takes an amount and a different User instance, and transfers money from the user's account into another user's account.'''