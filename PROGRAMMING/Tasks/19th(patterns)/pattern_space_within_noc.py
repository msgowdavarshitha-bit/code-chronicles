n=int(input("Enter the number: "))

noc=n  #number of stars on LHS
nol=n   #number of stars on RHS
for i in range(1,n+1):
    for j in range(1,n*2):

        if j<=nol or j>=noc:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    noc+=1
    nol-=1