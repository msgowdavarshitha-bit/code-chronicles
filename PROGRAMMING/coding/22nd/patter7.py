n=int(input("Enter: "))

for i in range(1,n+1):
    for j in range(1,n+1):

        if (i+j)%2==0:
            print(chr(64+j),end=" ")
        else:
            print(chr(96+j),end=" ")
    print()


# Enter: 4
# A b C d 
# a B c D 
# A b C d 
# a B c D 