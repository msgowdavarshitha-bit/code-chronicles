
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

