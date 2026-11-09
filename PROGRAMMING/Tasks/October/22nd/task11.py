n=int(input("Enter: "))


noc=n
for i in range(1,n*2):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(noc,1-1,-1):

        print(j,end="")
    print()

    if i<n:
        noc-=1
    else:
        noc+=1

# Enter: 4
# 4321
#  321
#   21
#    1
#   21
#  321
# 4321