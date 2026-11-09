n=int(input("Enter: "))

noc=1

for i in range(1,n*2):
    for k in range(n,noc,-1):
        print(" ",end="")
    for j in range(n,n-noc,-1):
        print(j,end="")
    print()

    if i<n:
        noc+=1
    else:
        noc-=1

# Enter: 5
#     5
#    54
#   543
#  5432
# 54321
#  5432
#   543
#    54
#     5





count=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(count,end=" ")
        count+=1
    print()


# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15 