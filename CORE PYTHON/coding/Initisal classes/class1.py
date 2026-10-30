class Student:
    def __init__(self):
        self.name="Varshitha"
        self.usn="4HG22cs051"
        self.qual="BE"
        self.height=5.2
        self.weight=45
    def eat(self):
        print("Im eating")
    def sleep(self):
        print("Im sleeping")
    def study(self):
        print("Im preparing... and best of luck............! ")
s1=Student()
print(s1.name)
print(s1.usn)
print(s1.qual)
print(s1.height)
print(s1.weight)


print("\nproperties addition like add new properties")
s1.address="Hassan"
s1.mob=9827383980
print(s1.address)
print(s1.mob)


print("\nupdating the already existing properties with new value")
s1.usn="4HG22CS001"
s1.name="Raama"
print(s1.usn)
print(s1.name)


print("\nStore the reference variable in an another variable so that both point to the same memory location where the class object is stored any updation made will effect each of them.")
s2=s1
s3=s1
print(s3.name)
print(s1.usn)



print("\n Every variables are considered to be a object so that when we print type(variable) it will give us the <class 'Type_of_value_that_variable _is storing")
a=20
print(a)
print(type(a))
b=90.00
print(b)
print(type(b))
c="hi"
print(c)
print(type(c))
d=[1,2]
print(d)
print(type(d))
e=(1,2,3,4)
print(e)
print(type(e))


