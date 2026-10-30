class BankAccount:
    bank_name = "KGS Bank"
    total_accounts = 0

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        BankAccount.total_accounts += 1

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully.")
        else:
            print("Enter a valid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Amount withdrawn successfully.")

    def display(self):
        print("Bank Name:", BankAccount.bank_name)
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)
        print("-" * 50)


def createAccount(n):

    if n == 0:
        return

    print("\nEnter details of account holder", n)

    name = input("Enter account holder name: ")
    balance = int(input("Enter initial balance: "))

    d1 = BankAccount(name, balance)

    deposit_amount = int(input("Enter deposit amount: "))
    d1.deposit(deposit_amount)

    withdraw_amount = int(input("Enter withdrawal amount: "))
    d1.withdraw(withdraw_amount)

    createAccount(n - 1)

    print("\nAccount Details:", n)
    d1.display()


print("Welcome to KGS Bank")

n = int(input("Enter the number of bank account holders: "))

createAccount(n)

print("Total accounts created:", BankAccount.total_accounts)