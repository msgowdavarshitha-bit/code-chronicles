print("Write a program to reverse the integer for both positive and negative integer")


def integerReverse(n):
    temp=n

    if n<0:
        n=n*-1
    rev=0
    while n>0:
        digit=n%10
        rev=(rev*10)+digit
        n=n//10
    if temp<0:
        rev=rev*-1
    return rev 

n=int(input("Enter the number that you want to reverse"))
a=integerReverse(n)
print(a)
