n=int(input("Enter the number: "))

nol=1    #start row number
noc=(n*2)-1    #start column number
for i in range(1,n*2):
    for j in range(1,n*2):
        if j<=nol or j>=noc:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    if i<n:
        nol+=1
        noc-=1
    else:
        nol-=1
        noc+=1