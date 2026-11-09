n=int(input("Enter the number: "))

for i in range(n,1-1,-1):
    for j in range(n,1-1,-1):

        if i>j:
            print(chr(64+i),end=" ")
        else:
            print(chr(64+j),end=" ")
    print()




# Enter the number: 4
# D D D D 
# D C C C 
# D C B B 
# D C B A 