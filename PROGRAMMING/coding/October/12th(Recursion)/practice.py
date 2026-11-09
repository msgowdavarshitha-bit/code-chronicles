def reverse(n,rev):
    if n<=0:
        return rev

    digit=n%10
    rev=(rev*10)+digit
    n//=10

    return reverse(n,rev)



n=int(input("Enter the number: "))
a=reverse(n,0)
print(a)