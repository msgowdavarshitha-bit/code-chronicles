print("#3.write a program to display all asn and non asn present in a user defined range separately")


def count(n):
    count=0
    while n>0:
        n=n//10
        count+=1
    return count 

def isAsn(n):
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


n1=int(input("Enter the start of armstrong: "))
n2=int(input("Enter the end of the armstrong: "))

print("The armstrong numbers are: ")
for i in range(n1,n2+1):
    if isAsn(i):
        print(i,end=" ")

print("\nThe non-armstrong numbers are: ")
for i in range(n1,n2+1):
    if not isAsn(i):
        print(i,end=" ")


