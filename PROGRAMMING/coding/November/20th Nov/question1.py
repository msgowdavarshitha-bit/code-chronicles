print("WAP to convert all the lower case to upper case with minimal object creation")

def upperCaseCOnvert(s):
    res=""
    for i in range(0,len(s)):
        if "a"<=s[i]<="z":
            res=res+chr(ord(s[i])-32)
        else:
            res=res+s[i]

    return res


s=input("Enter the string: ")
result=upperCaseCOnvert(s)
print(result)