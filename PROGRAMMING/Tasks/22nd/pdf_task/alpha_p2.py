n=int(input("Enter the number: "))


for i in range(n,1-1,-1):
    for j in range(n,1-1,-1):

        if j>i:
            print(chr(64+j),end=" ")
        else:
            print(chr(64+i),end=" ")
    print()



# Enter the number: 5
# E E E E E 
# E D D D D 
# E D C C C 
# E D C B B 
# E D C B A 