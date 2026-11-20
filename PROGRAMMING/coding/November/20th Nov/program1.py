def toLOwerCase(s):
    res=""
    for i in range(0,len(s)):
        if "A"<=s[i]<="Z":
            res=res+chr(ord(s[i])+32)
        else:
            res=res+s[i]
    return res

# def toLowerCase_using_arrays(s):
    
#     l1=list(s)
#     print(l1)

#     for i in range(0,len(l1)):
#         if "A"<=l1[i]<="Z":
#             l1[1]=chr(ord(l1[i])+32)
#     return "".join(l1)
s=input("Enter the string: ")
result=toLOwerCase(s)
print(result)




print("=========================================================")

def toLowerCase_using_arrays(s):
    
    l1=list(s)
    # print(l1)

    for i in range(0,len(l1)):
        if "A"<=l1[i]<="Z":
            l1[i]=chr(ord(l1[i])+32)
    return "".join(l1)   #join is a in-build function converts any iterable objects into a string

s=input("Enter the string: ")
result=toLowerCase_using_arrays(s)
print(result)