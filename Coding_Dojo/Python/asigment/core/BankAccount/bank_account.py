class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance = 200) -> None: 
        self.int_rate = int_rate
        self.balance = balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        new_balence = self.balance + amount
        return new_balence
        # your code here
    deposit(new_balance, amount = 20)
    # def withdraw(self, amount):
    #     # your code here
    # def display_account_info(self):
    #     # your code here
    # def yield_interest(self):
    #     # your code here
