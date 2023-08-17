
class BankAccount:
    def __init__(self,int_rate, balance) -> None: 
        self.int_rate = int_rate
        self.balance = balance

    class User:
        def __init__(self, name, email):
            self.name = name
            self.email = email
            self.account = BankAccount(int_rate=0.02, balance=0)
        


    def make_deposit(self, amount):
        balance += amount
        print(f"Your Balance is ${amount}")

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount + 5
            print(f" Your new Balance: ${self.balance}")
        else:
            print("Insufficient funds")

    user1 = User("Mark","mark@email.com")
    user2 = User("Jim", "jim@email.com")