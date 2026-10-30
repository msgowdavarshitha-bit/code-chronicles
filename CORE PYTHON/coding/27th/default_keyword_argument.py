print("27-10-2026")

print("Default argument and keyword argument")

#self= hold address inside class
#reference variable = holds the address outside the class

#Variable + value == Arguments
#Variable === Parameter

#DEFAULT ARGUMENT :-- The variable along with the values in the method definition is called as default argument
#KEYWORD ARGUMENT:--- Calling the method with the variables along with the values is called as keyword argument


class Demo:
    def disp(self,x,y,z):
        print(x,y,z)
d1=Demo()
a,b,c=10,20,23
d1.disp(a,b,c)  # 10 20 23
d1.disp(b,c,a)  # 20 23 10    the values passed will be given in the same order to the method definition

# d1.disp()
# d1.disp(b,a)
#both gives error that how many formal parameter we have passed that much of values to be passed in the actual parameter
#parameter error

print("Solution:- Use default parameter")
class Demo:
    def disp(self,x=11,y=22,z=33):
        print(x,y,z)
d1=Demo()
a,b,c=10,20,23
d1.disp(a,b,c)  # 10 20 23
d1.disp(b,c,a)  # 20 23 10    the values passed will be given in the same order to the method definition

d1.disp()  #11 22 33
d1.disp(b,a) # 20 10 33

#here also order may change so

print("Solution:- assign the variable itself to the actual parameters")

class Demo:
    def disp(self,x,y,z):
        print(x,y,z)
d1=Demo()
a,b,c=10,20,23
d1.disp(a,b,c)  # 10 20 23
d1.disp(x=a,y=b,z=c)  # 10 20 30    
d1.disp(b,c,a)  #20 23 10

