n=int(input("Enter: "))

noc=1
for i in range(1,n*2):
    for j in range(1,noc+1):
        print(j*i,end=" ")
    print()

    if i<n:
        noc+=1
    else:
        noc-=1


#         Enter: 4
# 1 
# 2 4 
# 3 6 9 
# 4 8 12 16 
# 5 10 15 
# 6 12 
# 7 