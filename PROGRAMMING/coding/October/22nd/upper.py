n=int(input("NUmber: "))

for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print(chr(64+i),end=" ")
    print()


# NUmber: 4
# A A A A
# B B B
# C C
# D 