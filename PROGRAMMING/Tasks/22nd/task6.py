n=int(input("Enter the number: "))

for i in range(n,1-1,-1):
    for j in range(i,1-1,-1):
        print(chr(96+j),end=" ")
    print()