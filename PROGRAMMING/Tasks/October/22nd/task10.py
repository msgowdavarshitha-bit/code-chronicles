n=int(input("Enter the number: "))

noc=1
nor=(n*2)-1

for i in range(1,n*2):
    for j in range(1,n*2):

        if j<=noc or j>=nor:
            print(noc,end=" ")
        else:
            print(" ",end=" ")

    print()

    if i<n:
        noc+=1
        nor-=1
    else:
        noc-=1
        nor+=1


# Enter the number: 4
# 1           1 
# 2 2       2 2 
# 3 3 3   3 3 3 
# 4 4 4 4 4 4 4 
# 3 3 3   3 3 3 
# 2 2       2 2 
# 1           1 