print("Write a program the given number is an integer palindrome or not")
#A number is said to ber an integer palindrome only when reversal of a number is same as the original number
#EG:- 101    -> 101
#      -2002   -> -2002 
#     -89    --> -98  is not an palindrome
#     45  ---> 54   it is not an integer palindrome bcz original is same as palindrome 


def isPalindrome(n):
    temp=n
    if n<0:
        n=n*-1
    p=0

    while n>0:
        digit=n%10
        p=(p*10)+digit
        n=n//10
    if temp<0:
        p=p*-1
    return p==temp

n=int(input("Enter the number: "))
if isPalindrome(n):
    print("It is a palindrome")
else:
    print("The given number is not a palindrome")