n=int(input("Enter the number: "))

for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end="")
    for j in range(n):
        print("*",end="")
    print()