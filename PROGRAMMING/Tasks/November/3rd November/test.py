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


n=17
if isPrime(n):
    print("It is prime")
else:
    print("It is not prime")



print()
def isPrime(n,i):
    if i*i>=n:
        return 

    i=1
    count=0
    while i*i<=n:
        if n%i==0:
            count+=1
            if i!=(n//i):
                count+=1
    return isPrime(n,i+1)


n=17
if isPrime(n,1):
    print("It is prime")
else:
    print("It is not prime")







