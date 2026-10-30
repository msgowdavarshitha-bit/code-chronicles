#break down expression to simplest task/form 
print("Nth factorial using recursion")



def fact(n):

    if n<=0:
        return 1
    return (n*fact(n-1))   #when we want to return it for the next logic return it / function call 



n=int(input("Enter the number: "))
print(fact(n))