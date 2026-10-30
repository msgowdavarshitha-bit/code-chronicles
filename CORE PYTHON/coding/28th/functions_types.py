print("Types of functions")

print("1.User defined \n 2.Built-in")
print("Types of user defined")


print("\n1.No parameter no return value")
def fun1():
    a,b=10,20
    print(a+b)
fun1()



print("\n2.No parameter return value")
def fun1():
    a,b=10,20
    return a+b
a=fun1()
print(a)


print("\n3.With parameter no return value")
def fun1(a,b):
    print(a+b)

x,y=10,20
fun1(x,y)


print("\n4.With parameter and  return value")
def fun1(a,b):
    return a+b

x,y=10,20
b=fun1(x,y)
print(b)

#NOTE :- activation record is deleted once it returns to the function where it is called (thats it) 
#        if there is no return inside the function PVM will assign the default return 