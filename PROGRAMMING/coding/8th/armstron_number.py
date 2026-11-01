print("DATE:-08-10-2026")
#Write a program to check whether the given number is an armstrong number number or not

print("Armstrong number:- If the sum of the exponent value(Base:- is each is each digit, power:- is total count of digits in a given number) of al, the digits individually in a given number is same as original number ")

def countDigit(n):
    count=0 
    while n>0:   #if any number which has the in-between 0 then it will stop loop so use n>0: not n>=0
        n=n//10 
        count+=1
    return count 


def isArmstrongNUmber(n):
    temp=n
    pow=countDigit(n)
    asn=0

    while n>0:
        base=n%10
        asn=asn+(base**pow)
        n=n//10
    return asn==temp


n=int(input("Enter the number: "))
if isArmstrongNUmber(n):
    print(n, 'Its a armstrong number')
else:
    print(n,"It is not an armstrong number")





#count will tell me what are remaining counts are remaining  
#series will tell me how range is going through



