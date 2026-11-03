n=int(input("ENter the number: "))

for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print(i,end="")
    print()


# ENter the number: 4
# 1111
# 222
# 33
# 4