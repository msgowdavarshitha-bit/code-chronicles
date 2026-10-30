n=int(input("Num: "))

count=1
for i in range(n,1-1,-1):
    for j in range(1,n+1):
        print(chr(96+count),end=" ")
        count+=1

        if count>26:
            count=1
    print()

