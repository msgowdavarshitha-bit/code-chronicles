n=int(input("ENter the value:"))

for i in range(1,n+1):
    for j in range(i,1-1,-1):
        print(j,end="")
    print()


# ENter the value:4
# 1
# 21
# 321
# 4321