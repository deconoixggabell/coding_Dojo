# class user:
#     def __init__(self) -> None:
#         self.first_name = "ada"
#         self.last_name = "cage"
#         self.age = 10

# user_ada = user()
# print(user_ada.age)


class shoe:
    def __init__(self,brand, type, size, price) -> None:
        self.brnad = brand
        self.type = type
        self.size = size
        self.price = price

sheo1 = shoe("josef", "dress shoe", 9, 20 )
sheo2 = shoe("Nike", "sport shoe", 9, 60 )
print(f"{sheo1.type}, - {sheo2.type}")

class user:
    def __init__(self, name, email, age) -> None:
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        print(f"hello {self.name} nice to meet you")

adrian = user("adrian hugo", "hugo@email.com", 10)
print(f"{adrian.name} - {adrian.email} - {adrian.age}")
adrian.greeting()

class shoe:
    def __init__(self, brand, shoe_type, price) -> None:
        self.brand = brand
        self.shoe_type = shoe_type
        self.price = price
        self.in_stock = True

skate_shoe = shoe("Nike", "low traniner", 50)
dress_shoe = shoe("Joseph", "High top", 75)

skate_shoe.price = skate_shoe.price * (1 - 0.1) # type: ignore
dress_shoe.price = dress_shoe.price * (1 - 0.2) # type: ignore
print(f" the new price of {skate_shoe.brand} {skate_shoe.price} - the new price of  {dress_shoe.brand} {dress_shoe.price}")

# Methods

class Bank_Account:
    bank_name = "First Bank Of Dojo"
    all_account = []

    def __init__(self, int_rate, balance) -> None:
        self.int_rate = int_rate
        self.balance = balance
        Bank_Account.all_account.append(self)
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name

    @classmethod
    def all_balance(cls):
        sum = 0

        for account in cls.all_account:
            sum += account.balance
        return sum


class BankAccount:
    # ... __init__ goes here
    def with_draw(self,amount):
        # we can use the static method here to evaluate
        # if we can with draw the funds without going negative
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self
    # static methods have no access to any attribute
    # only to what is passed into it
    @staticmethod
    def can_withdraw(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

