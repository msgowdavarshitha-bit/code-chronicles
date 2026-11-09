n=int(input("Enter the number: "))

for i in range(n,1-1,-1):
    for j in range(n,1-1,-1):

        if i>j:
            print(chr(96+j),end=" ")
        else:
            print(chr(96+i),end=" ")
    print()

# Enter the number: 4
# d c b a 
# c c b a 
# b b b a 
# a a a a 