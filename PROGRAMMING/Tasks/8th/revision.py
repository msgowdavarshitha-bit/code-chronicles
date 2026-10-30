#to print armstrong or not

def countDigits(n):
    count=0
    while n>0:
        n=n//10
        count+=1
    return count

def isArmstrong(n):
    temp=n
    if n<0:
        n=n*-1
    asn=0
    pow=countDigits(n)

    while n>0:
        digit=n%10 
        asn=(digit**pow)+asn
        n=n//10 
    if temp<0:
        asn=asn*-1
    return asn==temp


n=int(input("Enter a number that you wanna check it as a armstrong number or not: "))
if isArmstrong(n):
    print(n,"It is a Armstrong number")
else:
    print(n,"is not an armstrong number")


print("\n")
print("*****"*9)
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
count=int(input("Enter the number: "))
series=1
print("The first",n,"armstrong numbers are: ")
while count>0:
    if isArmstrongNUmber(series):
        print(series,end=" ")
        count-=1
    series+=1