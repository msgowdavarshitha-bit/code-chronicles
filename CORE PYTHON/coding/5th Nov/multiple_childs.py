class A:
    def __init__(self):
        self.a=200

class B:
    def __init__(self):
        A.__init__(self)
        self.b=450

class C:
    def __init__(self):
        B.__init__(self)
        self.c=250

c1=C() #creating object for latest child C
print(c1.c)
print(c1.b)
print(c1.a)

#If we have multiple child classes create the object for the latest updated child class