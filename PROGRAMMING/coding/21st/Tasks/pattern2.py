n=int(input("Enter the number: "))


count=0
result=0

for i in range(n,1-1,-1):
    count+=i


for i in range(n,1-1,-1):
    for j in range(1,i+1):
        if i%2==0:
            print(count,end=" ")
            result=count
        else:
            print(result,end=" ")
            result+=1
        count-=1
    print()

    result=count-i+2