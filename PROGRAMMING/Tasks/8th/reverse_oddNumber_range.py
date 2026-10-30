print("3.Write a program to reverse only the odd the numbers present in a used defined range")

#a=97  b=102    only odd should be reversed 79 98 99 100 101 102

def isPalindrome(n):
    rev=0

    while n>0:
        digit=n%10
        rev=(rev*10)+digit
        n=n//10
    return rev 



n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))

print("The odd palindrome numbers within the range provided are:  ")

for i in range(n1,n2+1):
    if i%2!=0:
        print(isPalindrome(i),end=" ")
    elif i%2==0:
        print(i,end=" ")

