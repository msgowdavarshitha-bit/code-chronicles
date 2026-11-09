print("Types of variables ")

#within method inside class --> variable with self is a =--> instance variable
#outside class --> reference variable.method ==> instance variable
#USe self and reference variable


#Static variable:-
#declared within class before __init__ method
#Use:- can be used by all the methods
#WE can access this in all the methods and outside class


#Local variable
#variables within method without the self keyword is called as local variable
#we cannot access the local variable outside the class as well as outside method also


class Demo:
    x=10
    def __init__(self):
        self.a=100
    def disp(self):
        b=20
        print(b)

d1=Demo()
print(Demo.x)  #Static variable accessing outside the class
print(d1.a)   # Instance variable accessing outside the class using reference_var.static_var
d1.disp()     #method calling outside the function

#We cannot access the local variable bcz once the method executed the activation record is deleted