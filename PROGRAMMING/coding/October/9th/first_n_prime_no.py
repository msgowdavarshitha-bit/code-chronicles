def isPrime(n):
    if n<2:
        return False
    i=1
    count=0
    while i*i<=n:
        if n%i==0:
            count+=1
            if i!=(n//i):
                count+=1
        i+=1
    return count==2

n=int(input("Enter the number of prime numbers you want: "))
series=2
while n>0:
    if isPrime(series):
        print(series,end=" ")
        n-=1
    series+=1



print("========="*3)
def isPrime(n):
    if n<2:
        return False
    i=1
    count=0
    while i*i<=n:
        if n%i==0:
            count+=1
            if i!=(n//i):
                count+=1
        i+=1
    return count==2

n=int(input("Enter the number of prime numbers you want: "))
series=2
while n>0:
    if not isPrime(series):
        print(series,end=" ")
        n-=1
    series+=1