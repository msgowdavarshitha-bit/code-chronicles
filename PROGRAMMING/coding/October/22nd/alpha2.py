n=int(input("Enter the number: "))

for i in range(n,1-1,-1):
    for j in range(n,1-1,-1):
        if (j<i):
            print(j,end=" ")
        else:
            print(i,end=" ")
    print()




# Enter the number: 4
# 4 3 2 1 
# 3 3 2 1 
# 2 2 2 1 
# 1 1 1 1 