print("#the given number is prime or not  boolean value return")


def isPrime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    return count==2
n=int(input("Enter the number: "))
a=isPrime(n)
print(a)

#When we want to return the boolean value 