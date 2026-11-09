print("Passing function as a parameter")

print("Is called as higher order function -- Passing function as a parameter")


def func1():
    print("func1 is invoked")

def func2(a,b):
    c=a*b
    print(c)

def disp(ptr1,ptr2):
    ptr1()
    ptr2(10,2)


ptr3=func1
ptr4=func2

ptr3()   #
ptr4(5,2) #  both are called as first class function
disp(ptr3,ptr4)

#func2 == ptr4 ==  ptr2  --> func2
#func1 == ptr1 == ptr1   --> func1

