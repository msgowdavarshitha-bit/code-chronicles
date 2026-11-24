# def numConversion(s):
#     sumNum=0
#     nstr=""
#     for i in range(0,len(s)):
#         if "0"<=s[i]<="9":
#             sumNum=sumNum+(ord(s[i])-48)
#         else:
#             nstr+=s[i]
        
#     nNum=""
#     while sumNum>0:
#         rem=sumNum%10
#         nNum=chr(rem+48)+nNum
#         sumNum//=10
    
#     return nstr+nNum

#using inbuilt function
def numConversion(s):
    sumNum=0
    nstr=""
    for i in range(0,len(s)):
        if "0"<=s[i]<="9":
            sumNum=sumNum+(ord(s[i])-48)
        else:
            nstr+=s[i]
    
    return nstr.str(sumNum)
    
s=input("Enter a string:")
res=numConversion(s)
print("Converted string:",res)

# Enter a string:1ad88c2
# Converted string: adc19

