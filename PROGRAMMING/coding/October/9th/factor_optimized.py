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






