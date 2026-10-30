def countDigit(n):
    count=0
    while n<=0:
        n=n//10
        count+=1
    return count

def isArmstrong(n,asn,pow,num):
    if n<=0:
        return asn==num
    digit=n%10
    asn=asn+(digit**pow)
    isArmstrong(digit,asn,n//10,num)    

n=int(input("Enter the number: "))
pow=countDigit(n)
if isArmstrong(n,0,pow,n):
    print("It is ANS")
else:
    print("It is not ANS")