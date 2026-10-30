print("Method returning a value")

class Demo:
    def add(self,a,b):
        c=a+b
        return c
    def sub(self,a,b):
        c=a-b
        return c
    def mul(self,a,b):
        c=a*b
        return c
d1=Demo()
x,y=10,20
r1=d1.add(x,y)
print(r1)
r2=d1.sub(x,y)
print(r2)
r3=d1.mul(x,y)
print(r3)


print("====="*10)
print("Method returning multiple value")
class Ret():
    def multiret(self,a,b):
        c=a+b 
        d=a-b
        e=a*b
        return c,d,e  #return multiple values 
        #return a+b,a-b,a*b   ---> also valid
d1=Ret()
x,y=10,20
r1,r2,r3=d1.multiret(x,y)  #when we return multiple values use multiple variable to hold it 
print(r1,r2,r3)
