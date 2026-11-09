print("Integer palindrome check")

def integer_palindrome(n):
    temp=n
    rev=0
    if n<0:
        n=n*-1

    while n>0:
        digit=n%10
        rev=(rev*10)+digit
        n//=10
    if temp<0:
        rev=rev*-1
    return rev==temp


n=int(input("Enter the number u want to check as a palindrome: "))
if integer_palindrome(n):
    print(n,"is a palindrome")
else:
    print(n,"It is not a palindrome")



print()
print("1st n Integer palindrome")

def integer_palindrome(n):
    temp=n
    rev=0
    if n<0:
        n=n*-1

    while n>0:
        digit=n%10
        rev=(rev*10)+digit
        n//=10
    if temp<0:
        rev=rev*-1
    return rev==temp

n=int(input("Enter the how many integer palindrome u want: "))
series=1
while n>0:
    if integer_palindrome(series):    #if non integer palindrome asked use if not integer_palindrome(series)
        print(series,end=" ")
        n-=1
    series+=1

#If asked to give separately give integer and non integer palindrome numbers
#same above first n logic but keep n in temporary variable and use separate while loop for palindrome and separate while loop with temp variable for non integer palindrome
#if given user range use for loop 
#if separately have to give means no need of separate temp variable use 2 for loop with range thats it 