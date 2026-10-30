print()
print("#1 to n in incrementing order :- without changing base condition and recursion and dont use the third variable")
#decrement it first then print it because when it reach the base condition true the function call will automatically return the local variable value there in the previous cycle and goes on

def display(n):
    if n<=0:  #Base condition:- stop condition   :- if we dont mention this it will not stop execution and through the redundancy error that indicates the end/stop/ base condition is not mentioned here and memory allocation is out of limit
        return
  
    display(n-1)
    print(n,end=" ")
    n-=1
    return

n=int(input("Enter the number: "))
display(n)