n=int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()


#     Enter the number: 4
# 1 1 1 1 
# 0 0 0 0 
# 0 0 0 0 
# 1 1 1 1 