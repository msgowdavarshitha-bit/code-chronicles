class Farmer:
    #static variable
    r=2.5  #this is the static variable where throughout class this value remains the same 
    #The variable value is fixed then it can be used as static variable
    #to save the memory allocation in the heap for every tome the object is called 
    #So in RAM in a static segment 2bytes of memory is allocated and it doesn't need to be stored in heap (EExtra fixed m/m will waste)
    #use the class object name while calculating  eg:- Farmer.r 

    
    def __init__(self,p1,t1):
        self.p=p1
        self.t=t1

    def calculate(self):
        s1=(self.p*self.t*Farmer.r)/100
        print(s1)

f1=Farmer(122,5)
f2=Farmer(2500,12)
f3=Farmer(10000,1)

f1.calculate()
f2.calculate()
f3.calculate()


