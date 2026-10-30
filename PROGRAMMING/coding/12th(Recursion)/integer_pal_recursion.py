print("Write a program to check number is palindrome or not  using recursion ")


def reverse(n,rev):
    if n<=0:
        return rev
    digit=n%10
    rev=(rev*10)+digit
    n=n//10
    return reverse(n,rev)


def isPalindrome(n,rev,temp):
    #Dont declare temp again here bcz u passed in the outside the function itself 
    if n<=0:
        return rev==temp
    digit=n%10
    rev=(rev*10)+digit
    n=n//10
    return isPalindrome(n,rev,temp)

n=int(input("Enter the number u want to check the palindrome: "))

res=reverse(n,0)
print("Reversed number",res)
if isPalindrome(n,0,n):  #here only passed temp
    print("it is a palindrome")
else:
    print("it is not a palindrome")




print()

print("To check it as palindrome or not no need of extra reverse function ")

def isPalindrome(n,rev,temp):
    #Dont declare temp again here bcz u passed in the outside the function itself 
    if n<=0:
        return rev==temp   # once it ends
    digit=n%10
    rev=(rev*10)+digit
    n=n//10
    return isPalindrome(n,rev,temp)

n=int(input("Enter the number u want to check the palindrome: "))

if isPalindrome(n,0,n):  #here only passed temp
    print("it is a palindrome")
else:
    print("it is not a palindrome")

