class Parent:
    def __init__(self):
        self.a=10


class Child:
    def __init__(self):
        self.b=20


c1=Child()   #create the object c1 for the child class
print(c1.b)
# print(c1.a)
# # print(c1.a)
#           ^^^^
# AttributeError: 'Child' object has no attribute 'a'



print()
print("solution")

class Parent:
    def __init__(self):
        self.a=10


class Child:
    def __init__(self):
        Parent.__init__(self)
        self.b=20


c1=Child()
print(c1.b)
print(c1.a)
