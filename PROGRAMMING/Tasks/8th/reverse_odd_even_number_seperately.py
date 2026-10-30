print("2.Write a program to reverse all the numbers present in a user defined range and display even and odd separately")

#a=97  b=102 even reversed:- 89 1 201, odd reversed:- 79 99 101

def isReverse(n):
    rev=0

    while n>0:
        digit=n%10 
        rev=(rev*10)+digit
        n=n//10
    return rev

n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))



print("The even numbers reversed are: ")
for i in range(n1,n2+1):
    if i%2==0:
        print(isReverse(i),end=" ")


print("\nThe odd numbers reversed are: ")
for i in range(n1,n2+1):
    if i%2!=0:
        print(isReverse(i),end=" ")
