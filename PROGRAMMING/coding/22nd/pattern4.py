n=int(input("Num: "))

for i in range(n,1-1,-1):
    for j in range(n,n-i,-1):
        print(chr(96+j),end=" ")
    print()


# Num: 4
# d c b a 
# d c b 
# d c 
# d 