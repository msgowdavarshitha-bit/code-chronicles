def countDigit(n):
    count=0
    while n>0:
        n=n//10
        count+=1
    return count
def isASN(n):
    temp=n
    pow=countDigit(n)
    asn=0
    if n<0:
        n=n*-1

    while n>0:
        base=n%10
        asn=asn+(base**pow)
        n=n//10
        if temp<0:
            asn=asn*-1
    return asn==temp


n=int(input("Enter: "))
if isASN(n):
    print("ASN")
else:
    print("not ASN")