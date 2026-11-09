n=int(input("Enter the number: "))
noc=1

for i in range(1,n*2):
    for k in range(1,noc+1):
        print(" ",end="")

    for j in range(noc,n+1):
        print(j,end=" ")
    print()

    if i<n:
        noc+=1
    else:
        noc-=1


# Enter the number: 4
#  1 2 3 4 
#   2 3 4 
#    3 4 
#     4 
#    3 4 
#   2 3 4 
#  1 2 3 4 