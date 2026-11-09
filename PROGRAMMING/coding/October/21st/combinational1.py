n=int(input("Enter the number: "))

noc=1

for i in range(1,n*2):
    for j in range(n,noc-1,-1):
        print(j,end="")
    print()

    if i<n:
        noc+=1
    else:
        noc-=1


#     Enter the number: 4
# 4321
# 432
# 43
# 4
# 43
# 432
# 4321