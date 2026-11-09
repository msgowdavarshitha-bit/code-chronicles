print("to display first n integer palindrome")
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




n=int(input("Enter a number: "))
series=1

while n>0:
    if isPalindrome(series):
        print(series,end=" ")
        n=n-1
    series+=1