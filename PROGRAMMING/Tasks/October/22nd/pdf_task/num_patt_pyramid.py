n=int(input("Enter: "))


for i in range(1,n+1):
    
    for j in range(1,i*2):
        if i>=j:
            print(j,end=" ")
            k=j
        else:
            print(k-1,end=" ")
            k-=1
    print()



# Enter: 5
# 1 
# 1 2 1 
# 1 2 3 2 1 
# 1 2 3 4 3 2 1 
# 1 2 3 4 5 4 3 2 1 