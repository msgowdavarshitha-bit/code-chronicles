pin=1234 
savings_balance=500
current_acc_balance=1000
print("Welcome to the ATM \nInsert your card here")

while True:
    insert_card=int(input("If the car is inserted if inserted 'Yes press 1' or else 'No press 0': "))
    if insert_card==1:
        break 
    elif insert_card==0:
        print("Please insert your card here") 


while True:
    p=int(input("Enter your 4 digit pin: "))
    if p==pin:
        break 
    else:
        print("Wrong PIN. Please enter the Correct PIN")

language=int(input("Enter your choice 1.English or 2.Hindi 3.Kannada: "))
if language==1 or language==2 or language==3:
    options=int(input("Enter the options 1.Withdraw  2.deposit   3.Balance check: "))
    if options==1:
        acc_type=int(input("Enter the bank account you want to withdraw \n 1.Savings   2.Current: "))
        if acc_type==1:
            while True:
                amt=int(input("Enter the amount to withdraw: "))
                if amt<=savings_balance:
                    print("Processing \n Please collect the cash")
                    break
                else:
                    print("You entered the amount more than your balance \n Please enter the valid amount")
            balance_amt_saving=savings_balance-amt 
            
        if acc_type==2:
            while True:
                amt=int(input("Enter the amount to withdraw: "))
                if amt<=current_acc_balance:
                    print("Processing \n Please collect the cash")
                    break
                else:
                    print("You entered the amount more than your balance \n Please enter the valid amount")
            balance_amt_current=current_acc_balance-amt 
    collect=int(input("Do you want to continue to check the savings bank balance press 1 \nto check your current bank balance press 2 \nTo exit press 3"))
    if collect==1:
        print(balance_amt_saving)
    if collect==2:
            print(balance_amt_current)
    if collect==3:
        print("Please collect your card \nTHANK YOU..:)")

    
    
    if options==2:
        acc_type=int(input("Enter the bank account you want to deposit \n 1.Savings   2.Current: "))
        if acc_type==1 or acc_type==2:
            cash=int(input("Enter the amount you want to deposit"))
            print("Please insert the cash inside")
            print("Processing please wait")
        deposit_balance=current_acc_balance+cash
    collect=int(input("Do you want to continue to check the balance press 1 or else press 2 "))
    if collect==1:
        print(deposit_balance)
        if collect==2:
            print("Please collect your card \nTHANK YOU..:)")


    if options==3:
        check_balance=int(input("Enter the account you want to check the balance \n1.Savings bank   2. current account"))
        if check_balance==1:
            print(savings_balance)
        elif check_balance==2:
            print(current_acc_balance)

    
                

                