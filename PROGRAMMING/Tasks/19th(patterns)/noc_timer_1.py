n=int(input("Enter the number: "))


noc=4

for i in range(1,n*2):

    for k in range(n-noc):
        print(" ",end="")
    for j in range(noc):
        print("* ",end="")
    print()

    if i<n:
        noc-=1
    else:
        noc+=1