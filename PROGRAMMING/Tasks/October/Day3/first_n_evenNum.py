print("2. WAL to print first n even numbers. ")

def evenNum(n):
    if n==0:
        return
    evenNum(n-1)
    print(2*n,end=" ")
    n-=1
    return

n=int(input("Enter a number: "))
evenNum(n)





