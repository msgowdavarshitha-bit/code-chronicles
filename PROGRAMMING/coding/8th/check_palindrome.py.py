print("1.Write a program to check the number is palindrome or not")


def integerPalindrome(n):
    temp=n
    if n<0:
        n=n*-1
    pal=0
    while n>0:
        digit=n%10
        pal=(pal*10)+digit
        n=n//10
    if temp<0:
        pal=pal*-1
    return pal==temp

num=int(input("Enter the number that you want to reverse"))
if integerPalindrome(num):
    print("It is a integer palindrome")
else:
    print("It is not a integer palindrome")




print("++++++"*5)
def integerPalindrome(n):
    temp=n
    if n<0:
        n=n*-1
    pal=0
    while n>0:
        digit=n%10
        pal=(pal*10)+digit
        n=n//10
    if temp<0:
        pal=pal*-1
    if pal==temp:
        return True 
    else:
        return False

num=int(input("Enter the number that you want to reverse"))
a=integerPalindrome(num)
print(a)


print("ASSIGNMENT")
# to display all the integer palindromes present in a user defined range


# to display all the non integer palindromes present in a user defined range

# to display all the integer palindrome and non integer palindrome present in a user  defined range separately
 #to display first n integer palindrome
 # to display first n non integer palindrome


