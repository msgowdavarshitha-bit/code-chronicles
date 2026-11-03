n=int(input("Enter a number: "))

for i in range(n,(1-1),-1):
    for k in range(n,i-1,-1):
        print(" ",end="")
    for j in range(1,n+1):
        print("*",end="")

    print() 



# Enter a number: 4
# ****
#  ****
#   ****
#    ****


print()
for i in range(1,n+1):
    for k in range(1,i):
        print(" ",end="")
    for j in range(1,n+1):
        print("*",end="")
    print()

#same no need of the decrementing loop 