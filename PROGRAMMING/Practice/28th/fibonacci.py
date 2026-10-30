def fib(num,n1,n2):
    if num<=0:
        return
    return fib(num-1,n2,n1+n2)





num=int(input("Enter: "))
fib(num,0,1)