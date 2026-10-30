
print("#CO-PRIME:-The given numbers are said to be co- prime If and only if the HCF/ GCD of the numbers is exactly 1")
print("to check whether the given 2 numbers are co-primes are not")




def findHCF(n1,n2):
    lower=n1
    if n2>n1:
        lower=n2 
    gcd=1
    for i in range(2,(lower+1)):   #Since we have initialized the gcd has 1 start loop from 2 so that one more waste of 
        if n1%i==0 and n2%i==0:
            gcd=i
    return gcd==1

n1=int(input("Enter the first input: "))
n2=int(input("Enter the second input: "))

if findHCF(n1,n2):
    print("The are co-primes")
else:
    print("They are not co-prime")