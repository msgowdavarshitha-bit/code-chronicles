print("#4.Write a program to display the first n asn")

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

n=int(input("Enter how many want a armstrong: "))

beg=1

print("The armstrong number till you mentioned are: ")

while n>0:
    if isASN(beg):
        print(beg, end=" ")
        n=n-1
    beg=beg+1
