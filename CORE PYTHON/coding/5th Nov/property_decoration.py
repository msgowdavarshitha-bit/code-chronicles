print("Property decorator")
#use method name for both setdata and getdata function name

class Person:
    def __int__(self):
        self.__name=""


    #we have to get the data bcz what if the value is already present so get data first and set it
    @property
    def dataaccess(self):
        return self.__name

    @dataaccess.setter
    def dataaccess(self,value):
        self.__name=value


p1=Person()
p1.dataaccess="Raama"
r1=p1.dataaccess

print(r1)