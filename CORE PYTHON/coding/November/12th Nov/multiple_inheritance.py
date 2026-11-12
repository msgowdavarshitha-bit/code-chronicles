print("MOR:- method resolution order -- To achieve the multiple inheritance in python")

class A:
    def display(self):
        print("A")

class B:
    def display(self):
        print("B")

class C(A,B):
    def disp(self):
        print("C")
        B.display(self)    #method resolution order using the this parent class method 

c1=C()
c1.disp()
c1.display()