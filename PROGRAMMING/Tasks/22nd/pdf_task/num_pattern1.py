n=int(input("Enter: "))

noc=1
for i in range(1,n*2):
    for j in range(1,noc+1):
        print(j,end="")

    print()

    if i<n:
        noc+=1
    else:
        noc-=1

# Enter: 5
# 1
# 12
# 123
# 1234
# 12345
# 1234
# 123
# 12
# 1