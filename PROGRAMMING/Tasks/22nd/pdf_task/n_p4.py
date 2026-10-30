n=int(input("Enter the number: "))

noc=1

for i in range(1,n*2):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(1,noc+1):
        print(j,end=" ")
    print()

    if i<n:
        noc+=1
    else:
        noc-=1


# Enter the number: 5
#     1 
#    1 2 
#   1 2 3 
#  1 2 3 4 
# 1 2 3 4 5 
#  1 2 3 4 
#   1 2 3 
#    1 2 
#     1 