print("Write a program to display first n asn numbers and non asn separately")

def count(n):
    count=0
    while n>0:
        n=n//10
        count+=1
    return count

def isASN(n):
    temp=n
    if n<0:
        n=n*-1
    asn=0
    pow=count(n)

    while n>0:
        digit=n%10
        asn=asn+(digit**pow)
        n=n//10
    if temp<0:
        asn=asn*-1
    return asn==temp 

n=int(input("Enter how many armstrong and non armstrong: "))
temp1=n    #in the while loop it is n is going till 0 that is positive number so it is when comes for non-asn it start and ed to 0 so for further reusability store n to temp1 before using it 
beg=1


print("The armstrong number till you mentioned are: ")

while n>0:
    if isASN(beg):
        print(beg, end=" ")
        n=n-1
    beg=beg+1



print("\nThe non armstrong number till you mentioned are: ")

beg=1   # here beg is went till last asn when we use it here again the loop or begining start from last armstrong not from 1 so 
while temp1>0:
    if not isASN(beg):
        print(beg, end=" ")
        temp1-=1
    beg=beg+1
