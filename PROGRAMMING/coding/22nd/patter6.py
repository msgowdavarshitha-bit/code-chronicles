n=int(input("ENte: "))

noc=(n*2)-1
for i in range(1,n+1):
    for j in range(1,n*2):
        if j<=i or j>=noc:
            print(chr(64+i),end=" ")
        else:
            print(" ",end=" ")
    print()
    noc-=1


# ENte: 4
# A           A 
# B B       B B 
# C C C   C C C 
# D D D D D D D 
    