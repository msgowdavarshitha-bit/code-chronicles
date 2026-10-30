print("Write a program to reverse the integer")


def integerReverse(n):
    
    rev=0
    while n>0:
        digit=n%10
        rev=(rev*10)+digit
        n=n//10
    return rev

n=int(input("Enter the number that you want to reverse"))
a=integerReverse(n)
print(a)
