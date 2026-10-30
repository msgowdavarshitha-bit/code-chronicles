print("TO print first n prime numbers")

def isPrime(n):
    count=0

    for i in range(1,n+1):
        if n%i==0:
            count+=1
    return count==2

n=int(input("Enter how many prime numbers do you need (from first): "))

series=2
while n>0:
    if isPrime(series):
        print(series,end=" ")

        n-=1
    series+=1
