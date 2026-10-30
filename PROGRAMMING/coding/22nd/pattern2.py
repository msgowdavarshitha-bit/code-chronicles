n=int(input("ENter: "))

for i in range(1,n+1):
    for j in range(n,1-1,-1):
        if i%2!=0:
            print(chr(96+j),end=" ")
        else:
            print(chr(64+j),end=" ")
    print()


# ENter: 4
# d c b a 
# D C B A 
# d c b a 
# D C B A 