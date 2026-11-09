def countDigit(n,count):
    if n<=0:
        return count
    return countDigit(n//10,count+1)

def isASN(n):
    temp=n
    power=countDigit(n,0)
    asn=0

    while n>0:
        base=n%10
        asn=asn+(base**power)
        n//=10
    return temp==asn


n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))

for i in range(n1,n2+1):
    if isASN(i):
        print(i,end=" ")





print()
print("ASN and Non-ASN")
def countDigit(n,count):
    if n<=0:
        return count
    return countDigit(n//10,count+1)

def isASN(n):
    temp=n
    power=countDigit(n,0)
    asn=0

    while n>0:
        base=n%10
        asn=asn+(base**power)
        n//=10
    return temp==asn


n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))

print("ASN")
for i in range(n1,n2+1):
    if isASN(i):
        print(i,end=" ")

print("\nNon ASN")
for i in range(n1,n2+1):
    if not isASN(i):
        print(i,end=" ")


#for first n ASN 
#same logic instead of using for loop
#after n1 and n2 :-  instead of for loop take while loop start from 1 and continue until n>0: amd increment series every time
#NOTE make sure that separate series for ASN and Non ASN should be taken




# def countDigit(n,count):
#     if n<=0:
#         return count
#     return countDigit(n//10,count+1)

# def isASN(n):
#     temp=n
#     power=countDigit(n,0)
#     asn=0

#     while n>0:
#         base=n%10
#         asn=asn+(base**power)
#         n//=10
#     return temp==asn


# n1=int(input("Enter the first number: "))
# n2=int(input("Enter the second number: "))

# for i in range(n1,n2+1):
#     if isASN(i):
#         print(i,end=" ")





print()
print("First n ASN and Non-ASN")
def countDigit(n,count):
    if n<=0:
        return count
    return countDigit(n//10,count+1)

def isASN(n):
    temp=n
    power=countDigit(n,0)
    asn=0

    while n>0:
        base=n%10
        asn=asn+(base**power)
        n//=10
    return temp==asn


n=int(input("Enter the first number: "))
temp=n

series1=1
print("ASN")
while n>0:
    if isASN(series1):
        print(series1,end=" ")
        n-=1
    series1+=1

series2=1
print("\nNon ASN")
while temp>0:
    if not isASN(series2):
        print(series2,end=" ")
        temp-=1
    series2+=1


