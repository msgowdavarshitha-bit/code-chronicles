print("We can modify the nonlocal as local and local as non local using local and nonlocal keywords")

def fun1():
    a=10
    b=20
    print(a)
    print(b)

    def func2():
        nonlocal a
        a=100
        b=30

        print(a)
        print(b)
    func2()
    print(a)   #even after coming out of func2 to make a as 100 we use nonlocal keyword along with variable a 

fun1()
#print(a)

