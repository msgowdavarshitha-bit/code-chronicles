def countDigits(n):
    count=0
    while n>0:
        n//=10
        count+=1
    return count

def isArmstrong(n):
    temp=n
    asn=0
    power=countDigits(n)

    while n>0:
        base=n%10
        asn=asn+(base**power)
        n=n//10

    return asn==temp
n=int(input("Enter the number to check whether it is Armstrong or not: "))
if isArmstrong(n):
    print(n," is an Armstrong number")
else:
    print(n,"The number is not an Armstrong number")