n=int(input("Enter the number: "))

for i in range(n,1-1,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


print("=="*10)

for i in range(1,n+1):
    for j in range(i,1-1,-1):
        print(j,end=" ")
    print()