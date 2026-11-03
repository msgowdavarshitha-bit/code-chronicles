n=int(input("Enter the number: "))

for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end="")
    for j in range(1,n+1):
        print("*",end="")
    print()


#Both are same

print()
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,n+1):
        print("*",end="")
    print()


# Enter the number: 4
#    ****
#   ****
#  ****
# ****