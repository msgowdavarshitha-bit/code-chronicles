n=int(input("Enter the number: "))


noc=4
for i in range(1,n*2):
    for j in range(1,noc+1):
        if i%2!=0:
            print(0,end=" ")
        else:
            print(1,end=" ")
    print()

    if i<n:
        noc-=1
    else:
        noc+=1


# Enter the number: 4
# 0 0 0 0 
# 1 1 1 
# 0 0 
# 1 
# 0 0 
# 1 1 1 
# 0 0 0 0 