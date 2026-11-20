print("WAP to convert all the lower case to upper case with minimal object creation")

def upperCaseCOnvert(s):
    l2=list(s)
    for i in range(0,len(l2)):
        if "a"<=l2[i]<="z":
            l2=l2+chr(ord(l2[i])+32)
    return "".join(l2)   


s=input("Enter the string: ")
result=upperCaseCOnvert(s)
print(result)