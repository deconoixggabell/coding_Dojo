
class BankAccount:
    def __init__(self,int_rate, balance) -> None: 
        pass
        self.int_rate = int_rate
        self.balance = balance

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
        


    def make_deposit(self, amount):
        self.account = int(amount)
        self.account += amount
        return
        # print(f"Your Balance is ${amount}")

    def withdraw(self, amount):
        if amount < self.account:
            self.account -= amount + 5
            # print(f" Your new Balance: ${self.account}")
        else:
            print("Insufficient funds")

user1 = User("Mark","mark@email.com")
user1.make_deposit(100)
print(f"User:{user1.name} Balance ${user1.account}")
# user1.withdraw(10)

print("--------------------")

user2 = User("Jim", "jim@email.com")
user2.make_deposit(1000)
print(f"User:{user2.name} Balance ${user2.account}")
# user2.withdraw(200)