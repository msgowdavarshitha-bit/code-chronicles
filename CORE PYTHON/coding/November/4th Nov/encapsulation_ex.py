class Person:

    def __init__(self):
        self.__name=""

    def setdata(self,value):
        self.__name=value

    def getdata(self):
        return self.__name

f1=Person()
f1.setdata("Raama")
result=f1.getdata()
print(result)