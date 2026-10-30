n=int(input("NUmber: "))

for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,n+1):
        print("*",end="")
    print()


print("+"*20)
for i in range(1,n+1):
    for k in range(1,i):
        print(" ",end="")
    for j in range(1,n+1):
        print("*",end="")
    print()

