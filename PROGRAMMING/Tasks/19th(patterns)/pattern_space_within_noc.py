n=int(input("Enter the number: "))

noc=n  #number of stars on LHS
nor=n   #number of stars on RHS
for i in range(1,n+1):
    for j in range(1,n*2):

        if j<=noc or j>=nor:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    noc-=1
    nor+=1