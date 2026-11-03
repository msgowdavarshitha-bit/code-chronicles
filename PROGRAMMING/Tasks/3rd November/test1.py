n=int(input("Enter: "))
noc=(n*2)-1

for i in range(1,n+1):
    for j in range(1,n*2):
        if j==noc or j==i or j==1 or j==(n*2)-1 or i==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    noc-=1
    

