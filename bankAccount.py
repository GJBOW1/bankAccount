# bankAccount Practice Assignment - Gregg Bowen

# If you imagine a banking system, and how the data is modeled, you may think, well, everything should be tied to the customer, in other words, the user. But users have accounts, and accounts have balances. This gives us the idea that maybe an account is its own class apart from the user class. But as we stated, it is not completely independent of the User class; accounts only exist because users open them.

# For this assignment, don't worry about putting any user information in the BankAccount class. We'll take care of that in the next lesson!

# Let's first just get some more practice writing classes by writing a new BankAccount class.

# The BankAccount class should have a balance. When a new BankAccount instance is created, if an amount is given, the balance of the account should initially be set to that amount; otherwise, the balance should start at $0. The account should also have an interest rate in decimal format. For example, a 1% interest rate would be saved as 0.01. The interest rate should be provided upon instantiation. (Hint: when using default values in parameters, the order of parameters matters!)

# The class should also have the following methods:

# deposit(self, amount) - increases the account balance by the given amount
# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
# display_account_info(self) - print to the console: eg. "Balance: $100"
# yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
# This means we need a class that looks something like the below.

# Create a BankAccount class with the attributes interest rate and balance

# Add a deposit method to the BankAccount class

# Add a withdraw method to the BankAccount class

# Add a display_account_info method to the BankAccount class

# Add a yield_interest method to the BankAccount class

# Create 2 accounts

# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)

# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)

# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info

# class User:
#     def __init__(self, id, name, age, location, email): 
#         self.id = id
#         self.name = name
#         self.age = age
#         self.location = location
#         self.email = email


class BankAccount:
    bank_name = "Big Money Bank"
    all_accounts = []
    
    def __init__(self, id, name, age): 
        self.id = id
        self.name = name
        self.age = age
        self.int_rate = 0.01
        self.balance = 100
        BankAccount.all_accounts.append(self)

    def deposit(self):
        self.balance += 42
        return self

    def withdraw(self):
        self.balance -= 37
        return self

    def display_account_info(self):
        print("-------------------")
        print("Bank:", self.bank_name)
        print("Account ID:", self.id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Account Balance:", round(self.balance, 2))
        print("Account Interest Rate:", self.int_rate)
        print("-------------------")
        return self

    def yield_interest(self):
        self.balance = (1 + self.int_rate) * self.balance
        return self


account1 = BankAccount(123456, "Gregg", 36)
account2 = BankAccount(7891011, "Tom", 29)


account1.deposit().deposit().deposit().withdraw().yield_interest().display_account_info()
account2.deposit().deposit().withdraw().withdraw().withdraw().withdraw().yield_interest().display_account_info()

