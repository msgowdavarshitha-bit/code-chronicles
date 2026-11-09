n=int(input("Enter: "))

count=0
for i in range(1,n*(n+1)//2+1):
    count+=1
    

for i in range(1,n+1):
    var=count-i
    for j in range(1,i+1):
        print(chr(var+j+64),end="")
    count-=i
    print()

# Enter: 4
# J
# HI
# EFG
# ABCD


print("+++++++++++++"*3)

n=int(input("Enter: "))

count=0
for i in range(1,n*(n+1)//2+1):
    count+=1
print(count)

for i in range(1,n+1):
    val=count-i+1
    for j in range(1,i+1):
        print(chr(64+val),end=" ")
        val+=1
    count-=i



    print()
 