n=int(input("Enter the number: "))

noc=(n*2)-1
nor=1
for i in range(n,1-1,-1):
    for j in range(1,n*2):

        if j<=nor or j>=noc:
            print(i,end=" ")
        else:
            print(" ",end=" ")
    print()
    noc-=1
    nor+=1

# 4           4 
# 3 3       3 3 
# 2 2 2   2 2 2 
# 1 1 1 1 1 1 1 