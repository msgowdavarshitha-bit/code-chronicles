print("Invoking a function through a variable")

def fun1():
    print("fun1 is invoked")

def fun2(a,b):
    c=a*b
    print(c)

print(fun1)   #address of the func1
print(fun2)     #address of the func2

fun1()          #func1 is called
fun2(10,30)      #func2 is called



#Store the function in a variable and call the function using that variable and now call using that variable
ptr1=fun1    #Store in address of function
print(ptr1)  #print address is function
ptr1()        #calling function using calling a variable


ptr2=fun2
print(ptr2)
ptr2(10,30)