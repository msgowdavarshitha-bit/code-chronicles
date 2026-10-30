print("#2.write a program to display all asn present in a user defined range")
def count(n):
    count=0
    while n>0:
        n=n//10
        count+=1
    return count

def isArmstrong(n):
    temp=n
    if n<0:
        n=n*-1
    pow=count(n)
    asn=0

    while n>0:
        digit=n%10
        asn=asn+(digit**pow)
        n=n//10
    if temp<0:
        asn=asn*-1
    return asn==temp


n1=int(input("Enter the start point of the armstrong"))
n2=int(input("Enter till where you want the armstrong"))
print("The armstrong numbers are: ")
for i in range(n1,n2+1):
    if isArmstrong(i):
        print(i,end=" ")
    if not isArmstrong(i):
        continue
