def countDigit(n,count=0):
    if n<=0:
        return count
    return countDigit(n//10,count+1)


def isASN(n,asn,pow,temp):
    if n<=0:
        return asn==temp
    base=n%10
    return isASN(n//10,asn+(base**pow),pow,temp)


n=int(input("ENter: "))
series=1
while n>0:
    if isASN(series,0,countDigit(series),series):
        print(series,end=" ")
        n-=1
    series+=1
