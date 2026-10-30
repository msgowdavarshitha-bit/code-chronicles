n=int(input("Enter the number: "))


noc=n
num=1

for i in range(1,n*2):

    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(1,noc+1):
        print(num,end=" ")
    print()

    if i<n:
        noc-=1
        num+=1
    else:
        noc+=1
        num-=1


# Enter the number: 4
# 1 1 1 1 
#  2 2 2 
#   3 3 
#    4 
#   3 3 
#  2 2 2 
# 1 1 1 1 