n=int(input("Enter the number: "))

num=1

for i in range(1,n+1):
    for j in range(n,1-1,-1):
        if i<j:
            print(1,end=" ")
        else:
            print(i,end=" ")
    print()


# Enter the number: 5
# 1 1 1 1 1 
# 1 1 1 2 2 
# 1 1 3 3 3 
# 1 4 4 4 4 
# 5 5 5 5 5 