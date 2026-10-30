def countDigit(n,count):
    if n<=0:
        return count
    return countDigit(n//10,count+1)

def isPrime(n):
    c=0

    i=1
    
    while i*i<=n:
        
        if n%i==0:
            c+=1

            if i!=(n//i):
                c+=1
        i+=1
    return c==2

n=int(input("Enter: "))
a=countDigit(n,0)
if isPrime(n):
    print("It is prime")
else:
    print("It is not a prime")

