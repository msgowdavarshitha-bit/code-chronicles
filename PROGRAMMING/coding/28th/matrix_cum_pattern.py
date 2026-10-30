n=int(input("Enter:  "))

c_odd=(n*2)-1
c_even=1
for i in range(1,n+1):
    val=i
    for j in range(1,n+1):
        print(chr(64+val),end=" ")

        if j%2!=0:
           val+=c_odd
        else:
            val+=c_even

    print()
    c_odd-=2
    c_even+=2



print("====="*5)

n=int(input("Enter: "))

for i in range(1,n+1):
    for j in range(1,n+1):
        start=(j-1)*n
        if j%2==0:
            print(chr(64+start+(n-i+1)),end=" ")
        else:
            print(chr(64+start+i),end=" ")
    print()

