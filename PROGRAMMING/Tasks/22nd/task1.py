n=int(input("Enter number: "))

for i in range(1,n+1):
    for j in range(1,n+1):
        if i>j:
            print(i,end=" ")
        else:
            print(j,end=" ")
    print()


# Enter number: 4
# 1 2 3 4 
# 2 2 3 4 
# 3 3 3 4 
# 4 4 4 4 