n=int(input("Enter a number: "))

for i in range(1,n):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range((i*2),1,-1):
        print("*",end="")
    print()



# Enter a number: 4
#    *
#   ***
#  *****