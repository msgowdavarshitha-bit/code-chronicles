print("Prime")

def isPrime(n):
    i=1
    count=0
    while i*i<=n:
        if n%i==0:
            count+=1
            if i!=(n//i):
                count+=1
        i+=1

    return count==2


n=int(input("Enter the  umber of prime number you need: "))
series=1
while n>=0:
    if not isPrime(series):
        print(series,end=" ")
        n-=1
    series+=1


print("=================="*5)

def fibonacci(n):
    if n<=0:
        return n1
    while n>0:
        print(n1,end=" ")
        temp=n1+n2
        n1=n2
        n2=temp
        n-=1



n=int(input("enter the number: "))
fibonacci(n,0,1)



print("==========="*5)
def fibonacci(n,n1,n2):
    if n<=0:
        return
    print(n1,end=" ") 
    return fibonacci(n-1,n2,n1+n2)


n=int(input("enter the number: "))
fibonacci(n,0,1)





print("=========="*5)

def count(n,count):
    if n<=0:
        return count
    return count(n//10,count+1)

n=int(input("Enter: "))
count(n,0)