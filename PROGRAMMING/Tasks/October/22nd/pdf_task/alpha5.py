n=int(input("Enter: "))

for i in range(1,n+1):
    for j in range(1,n+1):
        start=(j-1)*n
        if j%2==1:
            print(chr(64+start+i),end=" ")
        else:
            print(chr(64+start+(n-i+1)),end=" ")
    print()




print("============================================================"*2)
print("Method 2")

n=int(input("Enter: "))

for i in range(1,n+1):
    for j in range(1,n+1):
        row=i
        if j%2==0:
            row=n-i+1
        print(chr(64+(j-1)*n+row),end=" ")
    print()

# A H I P 
# B G J O 
# C F K N 
# D E L M 