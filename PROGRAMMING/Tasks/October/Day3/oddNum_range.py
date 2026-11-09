print("1. WAL to display all the odd numbers present in a user defined range. ")


def isOdd(n):
    if n==0:
        return
    isOdd(n-1)
    print((2*n)-1,end=" ")
    n-=1
    return

n1=int(input("Enter first number: "))


isOdd(n1)

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

def isOdd(n):
    if n==0:
        return
    isOdd(n-1)
    print((2*n)-1,end=" ")
    n-=1
    return

n1=int(input("Enter first number: "))
n2=int(input("Enter first number: "))
for i in range(n1,n2+1):

    isOdd(i)
