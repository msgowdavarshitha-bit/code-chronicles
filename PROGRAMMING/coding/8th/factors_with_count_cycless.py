

print("FACTOR")
#an element is said to the factor of a number when the element is able to divide and reduce the number down to zero
#NOTE every factors of a number lie from 1 to the number itself
#All the factors of a given number will lie in the range of 1 to the number and itself
#least factor of a number is 1 and highest factor of a number is number itself


print("Write a program to print all the factors of a number")


def factors(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i,end=" ")

n=int(input("Enter the number"))
print("The factors of the given number is: ",n)
factors(n)



print("\n")
print("***"*5)
print("Write a program to print all the factors of a number and keep the count")


def count(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    return count


def factors(n):

    for i in range(1,n+1):
        if n%i==0:
            print(i,end=" ")
            a=count(i)
            

n=int(input("Enter the number"))
print("The factors of the given number is: ",n)
result=count(n)
print("The count of the factor is",result)
factors(n)



print("\n")
print("**"*10)

print("write a program to count thr enum of cycles taken to display/ count the factor of a given number")


def count(n):
    count=0
    cycles=0
    for i in range(1,n+1):
        cycles+=1
        if n%i==0:
           count+=1
        
    return count,cycles


def factors(n):

    for i in range(1,n+1):
        if n%i==0:
            print(i,end=" ")
            a=count(i)
            

n=int(input("Enter the number"))

print("The factors of the given number is: ",n)
factors(n)
result,cycle_result=count(n)    #WE can return the multiple values and call in the function call using 2 variables for that
print("\nThe count of the factor is",result)
print("The number of cycles: ",cycle_result)

#WE can return the multiple values and call in the function call using 2 variables for that


print("LOGIC 2")

print("all the factors of a given number can be displayed within the range of 1 to direct square root of the given number or lower nearest square root of the given number.")



