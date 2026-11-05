print("Property function in encapsulation")

#how to use setdata and getdata 

class Person:
    def __init__(self):
        self.name=""

    def setdata(self,value):
        self.__name=value

    def getdata(self):
        return self.__name

    getset=property(getdata,setdata)   #property is a predefined function that is used take getdata and setdata as a parametes

p1=Person()
p1.getset="Seetha"   #No need of paranthesis just use the getset which is same for getdata and setdata "=" is used to set the set the data
r1=p1.getset
#to get the data the setted data using p1(reference var) and get
print(r1)

