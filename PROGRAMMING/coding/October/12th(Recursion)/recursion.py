print("Write a program to print numbers from n(4) to 1 without using looping statements")
#maintain the code redundancy

print("RECURSION")
print("STACK TRACING")
#Stack is last in first out order 

def displayn4(n):
    print(n)
    displayn3(n-1)

def displayn3(n):
    print(n)
    displayn2(n-1)

def displayn2(n):
    print(n)
    displayn1(n-1)

def displayn1(n):
    print(n)


n=int(input("Enter th number: "))
displayn4(n)


print("Here also code and function redundancy is there")

print("Recursion ")
print("Base:- it is the condition that instruct where the function execution should stop ")


def display(n):
    if n<=0:  #Base condition:- stop condition   :- if we dont mention this it will not stop execution and through the redundancy error that indicates the end/stop/ base condition is not mentioned here and memory allocation is out of limit
        return
    print(n,end=" ")
    display(n-1)
   
    return

n=int(input("Enter the number: "))
display(n)




#Recursion is process of function calling itself for certain number of time
#Syntax1:- where there is no return value

#called function
#def fun_name(parameter):
    #base condition
    #logic
    #recursive function call'
#    fun_name(arguments)
#initial fun call
#fun_name(arguments)



#Syntax2:- where there is a return value

#called function
#def fun_name(parameter):
    #base condition
    #logic
    #recursive function call'
#   return  fun_name(arguments)
#initial fun call
#var_name=fun_name(arguments)


print("The condition which controls the recursive function call \nIt is decided based on when should the recursion call stop")

#REcursionError:-  it is thrown by the pvm when memory resource is asked beyond the availability

#it generally led in 2 case
#1. when i/p is very huge
#2. when there is a unlimited recursive call


#initial function call :- it is the first call of the function, without it no function will be executed
#in recursion ,the arguments passed should be the first value for the parameters
# it generally would be outside the recursive function which it is calling
# 
# recursive function call:-
# it is the call that is made to repeat the logic
# it is placed within which the function need to be repeated
# in recursion, the arguments passed should be the 
#       1.updated val that needs to be carry forward to the next cycle for further operations
#       2. the val which may not be updated but is required by the next cycle 



