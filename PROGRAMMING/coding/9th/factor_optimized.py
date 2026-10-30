print("#write a program to display all the factors of the given number")


def disFactors(n):
   
    i=1

    while i*i<=n:
        if n%i==0:
            print(i,end=" ")
            if i!=(n//i):
                print((n//i),end=" ")
        i+=1
    return i
    

def count(n):
    i=1
    countFactor=0
    countCycle=0
    while i*i<=n:
        countCycle+=1
        if n%i==0:
            countFactor+=1
            if i!=(n//i):
                countFactor+=1
                
        i+=1
    return countFactor,countCycle

n=int(input("Enter the number: "))
disFactors(n)
a,b=count(n)
print("\nNumber of factors are: ",a, "\nThe number of cycles are: ",b)







print("\n")
print("Prime numbers:- numbers has exactly 2 factors that is 1 and number itself")
print("Write a program to check whether the number is prime or not along with printing factors")
def isPrime(n):
    count=0
    i=1

    for i in range(1,n+1):
 
        if n%i==0:
            count+=1
            print(i,end=" ")
                
        i+=1
    return count==2


n=int(input("Enter the number: "))

if isPrime(n):
    print("\nIt is an prime number")
else:
    print("\nIt is not an prime number")



print("\n")
print("Write a program to check whether the number is prime or not along with printing factors along with number of factors and cycles")

def isPrime(n):
    count=0 
    print("The factors are: ")
    for i in range(1,n+1):
        if n%i==0:
            count+=1 
            print(i,end=" ")
    return count==2

def count(n):
    i=1
    countFactor=0
    countCycle=0
    while i*i<=n:
        countCycle+=1
        if n%i==0:
            countFactor+=1
            if i!=(n//i):
                countFactor+=1
                
        i+=1
    return countFactor,countCycle


n=int(input("Enter to the number to check: "))

if isPrime(n):
    print("\n",n,"is a prime number")
else:
    print("\n",n,"is not a prime number")

a,b=count(n)
print("The number of factors are",a)
print("The number of cycles are",b)