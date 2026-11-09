n=int(input("Enter a number: "))

noc=n
nor=n

for i in range(1,n+1):
    for j in range(1,n*2):
        if j>=nor or j<=noc:
            print(i,end=" ")
        else:
            print(" ",end=" ")
    print()
    noc-=1 
    nor+=1

# Enter a number: 4
# 1 1 1 1 1 1 1 
# 2 2 2   2 2 2 
# 3 3       3 3 
# 4           4 