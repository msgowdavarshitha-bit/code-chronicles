n=int(input("Enter the number: "))

count=1

for i in range(n,1-1,-1):
    for j in range(1,(n+1)):
        if i%2!=0:
            print("*",end=" ")
        else:
            print(count,end=" ")
        count+=1
    print()


#     Enter the number: 4
# 1 2 3 4 
# * * * * 
# 9 10 11 12 
# * * * * 