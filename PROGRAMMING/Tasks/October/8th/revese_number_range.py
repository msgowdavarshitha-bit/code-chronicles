print("1.Write a program to reverse all the numbers present in a user defined range")
#a=97  b=102 :=79 89 99 1 101 201 


def numReverse(n):
    temp=n 
    rev=0

    while n>0:
        digit=n%10 
        rev=(rev*10)+digit 
        n=n//10
    return rev 



n1=int(input("Enter first input: "))
n2=int(input("Enter second input: "))

print("Reversed numbers are: ")
for i in range(n1,n2+1):
    print(numReverse(i),end=" ")


#for i in range(n1,n2+1):
#   if numReverse(i):
#       print(i,end=" ")
# This will print the actual number itself like:- if numReverse(15)--> it will result numReverse(15) but when we print(i) --> this will actually print 15 (i) itself not the reversed number 
# Since inside the for loop it is 15 and it will also print 15 not the reversed value
#So use print(numReverse(i),end=" ") --> it will itself print the reversed number not the original actual value
