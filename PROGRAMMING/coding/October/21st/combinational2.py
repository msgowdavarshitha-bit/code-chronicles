n=int(input("Enter the number: "))

noc=n

for i in range(1,n*2):
    for j in range(1,noc+1):
        print(j,end="")
    print()

    if i<n:
        noc-=1
    else:
        noc+=1

#         Enter the number: 4
# 1234
# 123
# 12
# 1
# 12
# 123
# 1234