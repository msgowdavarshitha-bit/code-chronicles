print("1.Method is not taking parameter and not returning value")
class Demo:
    def __init__(self):
        self.name="V"
        self.age=10
    def disp(self):
        x=10
        y=20
        z=x+y
        print(z)   #30 here not returns the value in the method calling 
d1=Demo()
print(d1.name)
print(d1.age)


#Here not passing any parameter to the method disp and it not returning any values here and 'It will just execute the method thats it it doesn't mean it returned a value'
d1.disp()  

print("2.Method is not taking parameter but returning the value")
class Demo:
    def __init__(self):
        self.name="V"
        self.age=10
    def disp(self):
        x=10
        y=20
        z=x+y
        return z   #30 here not returns the value in the method calling 
d1=Demo()
print(d1.name)
print(d1.age)


#Here not passing any parameter to the method disp and it not returning any values here and 'It will just execute the method thats it it doesn't mean it returned a value'
r1=d1.disp()  
print(r1)




print("3.Method is taking parameter and not return the value")
class Demo:
    def __init__(self):
        self.name="V"
        self.age=10
    def disp(self,x,y):
        z=x+y
        print(z)   #30 here not returns the value in the method calling 
d1=Demo()
print(d1.name)
print(d1.age)


n1=100
n2=200
#Here not passing any parameter to the method disp and it not returning any values here and 'It will just execute the method thats it it doesn't mean it returned a value'
d1.disp(n1,n2)  






class Demo:
    def __init__(self):
        self.name="V"
        self.age=10
    def disp(self,x,y):
        z=x+y
        print(z)   #30 here not returns the value in the method calling 
d1=Demo()
print(d1.name)
print(d1.age)


#Here not passing any parameter to the method disp and it not returning any values here and 'It will just execute the method thats it it doesn't mean it returned a value'
d1.disp(100,200)   #the local variables with the values stored also be taken and directly values also can be passed




print("4.Methods with parameters and values are returned" )

class Demo:
    def __init__(self):
        self.name="V"
        self.age=10
    def disp(self,x,y):
        z=x+y
        return z   #30 here not returns the value in the method calling 
d1=Demo()
print(d1.name)
print(d1.age)


n1=100
n2=200
#Here not passing any parameter to the method disp and it not returning any values here and 'It will just execute the method thats it it doesn't mean it returned a value'
r1=d1.disp(n1,n2)  
print(r1)





print("*********"*5)
print("STANDARD WAY OF WRITING THE CLASS")


class Student:
    def __init__(self,n1,u1,m1,a1):
        self.name=n1
        self.usn=u1
        self.mob=m1
        self.add=a1
s1=Student("Raama","4hg22cs051",908765334,"Hassan")
s2=Student("Seetha","5hg23cd101",9078223930,"Bng")

print(s1.name)
print(s2.usn)