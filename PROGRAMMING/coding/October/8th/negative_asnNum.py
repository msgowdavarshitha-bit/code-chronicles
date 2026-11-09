print("For the negative number")
print("We can write it using absolute function first know about that function")
def countDigit(n):
    count=0 
    while n>0:
        n=n//10 
        count+=1
    return count 


def isArmstrongNUmber(n):
    temp=n
    if n<0:
        n=n*-1
    pow=countDigit(n)
    asn=0

    while n>0:
        base=n%10
        asn=asn+(base**pow)
        n=n//10
    if temp<0:
            asn=asn*-1
    return asn==temp


n=int(input("Enter the number: "))
if isArmstrongNUmber(n):
    print(n, 'Its a armstrong number')
else:
    print(n,"It is not an armstrong number")



