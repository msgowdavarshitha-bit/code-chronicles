n=int(input("Enter the number: "))

for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(i,1-1,-1):
        print(j,end="")
    print()



# Enter the number: 4
#    1
#   21
#  321
# 4321