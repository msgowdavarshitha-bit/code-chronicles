print("Types of inheritance: ")

#there are 4 types
#1.Single inheritance
#2. multi level inheritance
#3. Multiple inheritance
#4. hierarchial inheritance



print("1. Single inheritance")

class A:
    def dispA(self):
        print("A")

class B(A):
    def dispB(self):
        print("B")

b1=B()
b1.dispB()
b1.dispA()




print("==================================================="*2)

print("2. multi level inheritance")

class A:
    def dispA(self):
        print("A")

class B(A):
    def dispB(self):
        print("B")

class C(B):
    def dispC(self):
        print("C")       

b1=C()
b1.dispC()
b1.dispB()
b1.dispA()








print("==================================================="*2)

print("3. Hierarchial inheritance")

class A:
    def dispA(self):
        print("A")

class B(A):
    def dispB(self):
        print("B")

class C(A):
    def dispC(self):
        print("C")       

b1=B()
c1=C()
c1.dispC()
b1.dispB()
#Here is the multiple child has same parent and we can access parent using all the child
b1.dispA()
c1.dispA()