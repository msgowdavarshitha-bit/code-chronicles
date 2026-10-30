n=int(input("Enter number: "))


for i in range(n,1-1,-1):
    for j in range(n,1-1,-1):
        if i>j:
            print(i,end=" ")
        else:
            print(j,end=" ")
    print()



# Enter number: 4
# 4 4 4 4 
# 4 3 3 3 
# 4 3 2 2 
# 4 3 2 1 