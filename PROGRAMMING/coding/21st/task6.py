n=int(input("Enter the number: "))

noc=4

for i in range(n,(1-1),-1):
    for k in range(i-1):
        print(" ",end="")
    for j in range(n,noc+1,-1):
        print(j,end=" ")
    print()

    if i<n:
        noc-=1
    else:
        noc+=1