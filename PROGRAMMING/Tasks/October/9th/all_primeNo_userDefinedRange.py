print("TO display all the prime numbers in a user defined range")


def isPrime(n):
    count=0

    for i in range(1,n+1):
        if n%i==0:
            count+=1
    return count==2

n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))

for i in range(n1,n2+1):
    if isPrime(i):
        print(i,end=" ")
