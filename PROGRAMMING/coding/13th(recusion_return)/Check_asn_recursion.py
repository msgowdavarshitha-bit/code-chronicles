print("Write a program to check the number is armstrong or not using recursion")
def countRecur(n,count):
    if n<=0:
        return count
    
    return countRecur(n//10,count+1)  




def asnCheck(n,pow,asn,temp): #here we didn't mentioned base bcz base is a new value in every cycle and we don't want it to the next cycle or we are not using this base o/p to the next cycle

    if n<=0:
        return asn==temp

    base=n%10
    asn=asn+(base**pow)
    n=n//10

    return asnCheck(n,pow,asn,temp)


n=int(input("Enter the number: "))
pow=countRecur(n,0)
print("The number of counts are: ",pow)
if asnCheck(n,pow,0,n):
    print("It is an ASN")
else:
    print("It is not an ASN")


print()
print("Optimized")

def countRecur(n,count):
    if n<=0:
        return count
    
    return countRecur(n//10,count+1)  




def asnCheck(n,pow,asn,temp):

    if n<=0:
        return asn==temp

    base=n%10

    return asnCheck(n//10,pow,asn+(base**pow),temp)  #this is optimized


n=int(input("Enter the number: "))
pow=countRecur(n,0)
print("The number of counts are: ",pow)
if asnCheck(n,pow,0,n):
    print("It is an ASN")
else:
    print("It is not an ASN")












