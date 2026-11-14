print("METHOD OVERLOADING")

#python doesn't support method overloading

class Demo:
    def display(self,a):
        print(a)

    
    def display(self,a,b):
        print(a+b)

    def display(self,a,b,c):
            print(a+b+c)

c=Demo()


# c.display(10)
# c.display(10,20)

#  c.display(10)
# TypeError: Demo.display() missing 2 required positional arguments: 'b' and 'c'

c.display(10,20,300)




print("+============================================================+")

class Demo:
    def display(self,a):
        print(a)

    
    def display(self,a,b):
        print(a+b)

    def display(self,a,b,c):
            print(a+b+c)

c=Demo()


# c.display(10)
# c.display(10,20)
#  c.display(10)
# TypeError: Demo.display() missing 2 required positional arguments: 'b' and 'c'

# c.display(10,20,300)



#Solution
def f(*args):
    print(args)
f(10)
f(10,20)
f(10,20,30)



# def f1(**kwargs):
#     print(kwargs)
# f1(name="Raama",age=22)