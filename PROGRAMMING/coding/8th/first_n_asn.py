print("# 4.Write a program to display the first n asn ")
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
print("The first",count,"armstrong numbers are: ")
while count>0:
    if isArmstrongNUmber(series):
        print(series,end=" ")
        count-=1
    series+=1
