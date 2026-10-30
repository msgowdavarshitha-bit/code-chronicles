print("Write a program to display all the integer non integer palindromes present in a user defined range separately")

def isPalindrome(n):
    temp=n 
    if n<0:
        n=n*-1
    pali=0

    while n>0:
        digit=n%10
        pali=(pali*10)+digit
        n=n//10
    if temp<0:
        pali=pali*-1 
    return pali==temp




n=int(input("Enter first number: "))
n1=int(input("Enter the second number: "))


print("The palindromes in the given range are")
for i in range(n,n1+1):
    if isPalindrome(i):
        print(i,end=" ")

print("\nThe non palindromes in the given range are")
for i in range(n,n1+1):
    if not isPalindrome(i):
        print(i,end=" ")