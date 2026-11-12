class A:
    def __init__(self):
        self.a=10

class B(A):
    def __init__(self):
        self.b=20

class C(B):
    def __init__(self):
        self.c=40

c1=C()
print(c1.c)
# print(c1.b)   AttributeError: 'C' object has no attribute 'b'
# print(c1.a)




print("+=====+"*4)
print("Solution")


class A:
    def __init__(self):
        self.a=10

class B(A):
    def __init__(self):
        super().__init__()
        self.b=20
        

class C(B):
    def __init__(self):
        super().__init__()
        self.c=40
        


c2=C()
print(c2.c)
print(c2.b)   
print(c2.a)
