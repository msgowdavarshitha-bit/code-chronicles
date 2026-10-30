print("Types of variables")

a=10  #Global variable. if it is single it is local if it containing function it is global variable

def func1():
    print(a)
    b=20   #LOcal var
    print(b)

def func2():
    print(a)
    c=30  #local Var
    print(c)

    
print(a)   # global variable
func1()
#print(b)   #local variable we cannot access outside
func2()
#print(c)   #local variable we cannot access outside
print(a)