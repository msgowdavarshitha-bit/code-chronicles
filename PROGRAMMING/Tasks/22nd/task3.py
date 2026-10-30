n=int(input("Enter the number: "))

for i in range(1,n+1):
    for j in range(1,n+1):
        if i<j:
            print(chr(96+i),end=" ")
        else:
            print(chr(96+j),end=" ")
    print()


# Enter the number: 4
# a a a a 
# a b b b 
# a b c c 
# a b c d 