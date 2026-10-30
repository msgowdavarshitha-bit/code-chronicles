print("HCF / GCD: ")
print("Highest common factor / greatest common divisor")
print("For given 2 numbers which is the highest element that can commonly divide and reduce the input numbers down to zero that element said to be HCF")


#we cannot apply the square logic here



def findHCF(n1,n2):
    lower=n1
    if n2>n1:
        lower=n2 
    gcd=1
    for i in range(2,(lower+1)):   #Since we have initialized the gcd has 1 start loop from 2 so that one more waste of 
        if n1%i==0 and n2%i==0:
            gcd=i
    return gcd

n1=int(input("Enter the first input: "))
n2=int(input("Enter the second input: "))

a=findHCF(n1,n2)
print("The HCF is",a)


print("\n")
print("For the negative numbers")  
print("For negative numbers there is no HCF/GCD")

def findHCF(n1,n2):
    lower=n1
    if n2>n1:
        lower=n2 
    gcd=1
    for i in range(2,(lower+1)):   #Since we have initialized the gcd has 1 start loop from 2 so that one more waste of 
        if n1%i==0 and n2%i==0:
            gcd=i
    return gcd

n1=int(input("Enter the first input: "))
n2=int(input("Enter the second input: "))

a=findHCF(n1,n2)
print("The HCF is",a)



print("to display the gcd and hcd of given 2 numbers")
