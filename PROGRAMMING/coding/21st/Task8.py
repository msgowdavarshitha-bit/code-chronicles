n=int(input("Enter the number: "))

for i in range(n,1-1,-1):
    for k in range(i-1):
        print(" ",end="")
    for j in range(i,n+1):
        print(j,end=" ")
    print()


# Enter the number: 4
#    4 
#   3 4 
#  2 3 4 
# 1 2 3 4 