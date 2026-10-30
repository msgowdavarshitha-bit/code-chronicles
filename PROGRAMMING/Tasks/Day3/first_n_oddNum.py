print("3. WAL to print first n odd numbers. ")

def oddNum(n):
    if n==0:
        return 
    oddNum(n-1)
    print((2*n)-1,end=" ")

n=int(input("Enter the number: "))
oddNum(n)