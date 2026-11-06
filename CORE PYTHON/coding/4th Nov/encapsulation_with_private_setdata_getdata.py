class Book:

    def __init__(self):
        self.__pages=0    #__  ==> is to make the variable as private

    def setdata(self,value):      #to set the __pages value 
        if value>0:
            self.__pages=value    


    def getdata(self):    
        
        return self.__pages     #---> To return the settted data  

b1=Book()
# print(b1.__pages)   ---->  AttributeError: 'Book' object has no attribute '__pages'
b1.setdata(100)        #----> to set the __pages value to 100 as to update 
result=b1.getdata()    #-----> To get the updated value

print(result)




print("If given the -ve values dont set the value to the -ve given value")
class Book:

    def __init__(self):
        self.__pages=0    #__  ==> is to make the variable as private

    def setdata(self,value):
        if value>0:
            self.__pages=value    


    def getdata(self):    
        return self.__pages

b1=Book()
# print(b1.__pages)   ---->  AttributeError: 'Book' object has no attribute '__pages'
b1.setdata(-100)
result=b1.getdata()

print(result)