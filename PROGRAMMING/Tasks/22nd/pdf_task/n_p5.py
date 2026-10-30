n=int(input("Enter the number: "))


for i in range(1,n+1):
    for j in range(1,i+1):
        if j%2!=0:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()



#     Enter the number: 5
# 1 
# 1 0 
# 1 0 1 
# 1 0 1 0 
# 1 0 1 0 1 