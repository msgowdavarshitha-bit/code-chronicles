n=int(input("Enter the number: "))

for i in range(n,1-1,-1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print(i,end=" ")
    print()

#     Enter the number: 4
# 4 4 4 4
#  3 3 3
#   2 2
#    1 