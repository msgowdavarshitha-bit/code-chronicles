a=10
def func1():
    #print(a)  #UnboundLocalError: cannot access local variable 'a' where it is not associated with a value
    # this gives error checks it is present in the local and then global but we have used same variable so it 
    a=100
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


