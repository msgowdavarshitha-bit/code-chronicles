class A:
    def dispA(self):
        print("A")

class B(A):
    def dispB(self):
        print("B")

b1=B()
print(B.mro())  #class B->  A-> object class
print(A.mro())  #A-> object class