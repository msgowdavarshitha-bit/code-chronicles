def strRevLogic1(s):
    nstr=""
    for i in range(0,len(s)):
        nstr=s[i]+nstr
    return nstr

def strRevLogic2(s,nstr,i):
    if i>=len(s):
        return nstr
    
    nstr=s[i]+nstr
    return strRevLogic2(s,nstr,(i+1))

def strRevLog3(s):
    nstr=""
    for i in range((len(s)-1),0-1,-1):
        nstr=nstr+s[i]
    return nstr

def strRevLog4(s,nstr,i):
    if i<0:
        return nstr
    nstr=nstr+s[i]
    return strRevLog4(s,nstr,(i-1))

def strRevLog5(s):
    return "".join(reversed(s))

def strRevLog6(s):
    return s[::-1]

def strRevLog7(s):
    l1=list(s)
    i,j=0,len(s)-1
    
    while i<j:
        l1[i],l1[j]=l1[j],l1[i]
        i+=1
        j-=1
    return "".join(l1)

s=input("Enter a string:")
res1=strRevLogic1(s)
res2=strRevLogic2(s,"",0)
res3=strRevLog3(s)
res4=strRevLog4(s,"",len(s)-1)
res5=strRevLog5(s)
res6=strRevLog6(s)
res7=strRevLog7(s)
print("Reversed string using incrementing loop:",res1)
print("Reversed string using incrementing recc:",res2)
print("Reversed string using decrementing loop:",res1)
print("Reversed string using decrementing recc:",res2)
print("Reversed string using in-built fucn:",res5)
print("Reversed string using slicing:",res6)
print("Reversed string using swap:",res7)


# Enter a string:sky is blue
# Reversed string: eulb si yks

# Enter a string:apple is red
# Reversed string: der si elppa