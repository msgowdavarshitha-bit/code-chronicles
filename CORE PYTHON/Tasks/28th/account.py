
class BankAccount:
    bank_name = "KGS Bank"
    total_accounts = 0

    def __init__(self, account_holder, Balance):
        self.account_holder = account_holder
        self.Balance = Balance
        BankAccount.total_accounts += 1

    def deposit(self, amount):
        if amount > 0:
            self.Balance += amount
            print("Amount deposited successfully.")
        else:
            print("Enter a valid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid withdrawal amount.")
        elif amount > self.Balance:
            print("Insufficient balance.")
        else:
            self.Balance -= amount
            print("Amount withdrawn successfully.")

    def display(self):
        print("Bank Name:", BankAccount.bank_name)
        print("Account Holder:", self.account_holder)
        print("Balance:", self.Balance)
        print("-" * 50)


print(" Welcome to KGS Bank ")

n = int(input("Enter the number of bank account holders: "))

accounts = []

for i in range(1, n + 1):
    print("\nEnter details of account holder", i)

    name = input("Enter account holder name: ")
    balance = int(input("Enter initial balance: "))

    d1 = BankAccount(name, balance)

    accounts.append(d1)



for i in range(n):
    print("\nAccount Holder:", accounts[i].account_holder)

    deposit_amount = int(input("Enter deposit amount: "))
    accounts[i].deposit(deposit_amount)

    withdraw_amount = int(input("Enter withdrawal amount: "))
    accounts[i].withdraw(withdraw_amount)




for i in range(n):
    print("\nAccount Details", i + 1)
    accounts[i].display()

print("Total accounts created:", BankAccount.total_accounts)

