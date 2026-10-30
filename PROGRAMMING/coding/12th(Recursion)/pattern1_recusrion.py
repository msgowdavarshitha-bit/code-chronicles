
print()
print("TO display below series by getting user defined n")
#if n=4
#4 3 2 1 1 2 3 4
#No change in base condition, no change recursive function call
#3rd variable not accepted


def display(n):
    if n<=0:  #Base condition:- stop condition   :- if we dont mention this it will not stop execution and through the redundancy error that indicates the end/stop/ base condition is not mentioned here and memory allocation is out of limit
        return
    print(n,end=" ")
    display(n-1)
   
    return

n=int(input("Enter the number: "))
display(n)
