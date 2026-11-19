def fun1():
    print("entering func1")
    try:
        fun2()
    except Exception as e:
        print("Error in fun1")
    print("leaving fun1")    
    
def fun2():
    print("entering fun2")
    c=10/0
    print(c)
    print("Leaving fun2")
print("program started")    
fun1()
print("Program ended")