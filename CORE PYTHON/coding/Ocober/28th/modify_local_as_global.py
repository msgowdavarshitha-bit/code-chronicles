print("Modify the local variable into global variable. ")
a=10
def func1():
    #print(a)  #UnboundLocalError: cannot access local variable 'a' where it is not associated with a value
    # this gives error checks it is present in the local and then global but we have used same variable so it 
    
    #Solution
    global a   #global variable conversion using global keyword
    a=100
    print(a)
    b=20   #LOcal var
    print(b)

def func2():
    a=7000
    print(a)
    c=30  #local Var
    print(c)

    
print(a)   # global variable
func1()
#print(b)   #local variable we cannot access outside
func2()
#print(c)   #local variable we cannot access outside
print(a)


#NOTE:- The value that is declared as global and modified then the changes are global itself not local


# Modify the local variable into global variable. 
# 10
# 100  ----> Here we changed it 10 to 100
# 20
# 7000  ----> Here local a value inside 2nd def function
# 30
# 100     ----> Here also changed as 100