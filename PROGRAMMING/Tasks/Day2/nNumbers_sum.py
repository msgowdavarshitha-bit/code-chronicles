print("WAP to enter the numbers till the user wants and at the end it should display the sum of all the entered numbers. The loop should work until the user enter 0. ")


result=0
while True:
    n=int(input("Enter the number: "))
    if n==0:
        break
    result+=n
print(result)