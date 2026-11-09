print("Palindrome")

print("Write a program to display all the integer palindromes present in a user defined range")


def integerPalindrome(n):
    temp=n 
    if n<0:
        n=n*-1
    pal=0

    while n>0:
        digit=n%10
        pal=(pal*10)+digit
        n=n//10
    if temp<=0:
        pal=pal*-1
    return pal==temp


num1=int(input("Enter the first number: "))
num2=int(input("Enter the last number: "))

print("Palindromes within the provided range are: ")
for i in range(num1,num2+1):
    if integerPalindrome(i):
        print(i,end=" ")

