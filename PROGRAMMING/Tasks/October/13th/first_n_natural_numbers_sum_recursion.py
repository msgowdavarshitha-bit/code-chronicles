
def natural(n):
    if n<=0:
        return
    return n + natural((n-1))
    


n=int(input("Enter a number: "))
natural(n)