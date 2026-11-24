def strFilter(s):
    nstr=""
    for i in range(0,len(s)):
        if "A"<=s[i]<="Z":
            nstr=nstr+chr(ord(s[i])+32)
        elif ("a"<=s[i]<="z") or ("0"<=s[i]<="9"):
            nstr+=s[i]
            
    return nstr

def isStrPalindrome(s):
    s=strFilter(s)
    i,j=0,len(s)-1
    while i<j:
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True

s=input("Enter a string:")
if isStrPalindrome(s):
    print("It is string palindrome")
else:
    print("It is not string palindrome")
    
# Enter a string:?M1 aDA1,m
# It is string palindrome

# Enter a string:?a2,b?cE1:eD,B2A
# It is not string palindrome