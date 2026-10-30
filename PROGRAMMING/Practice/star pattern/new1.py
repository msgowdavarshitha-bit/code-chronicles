n=int(input("Enter the input: "))

noc=7

for i in range(n,1-1,-1):
    for j in range(1,n*2):
        if j<=i or j>=noc:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    noc-=1