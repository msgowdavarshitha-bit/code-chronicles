print("Aggregation:-")
print("without main object other objects can servive is called as aggregate object and the process is called as aggregation")

class Charger:
    def __init__(self, name):
        self.cname=name
        print("charger is ready")
    def getcharger(self):
        print(" charger is ready to connect ")

class Mobile:
    def __init__(self,name):
        self. mname=name
        self.C1=""    
        print("mobile is ready")  
        
    def hasmobile(self,c):
        self.C1=c
        print(" both are ready to connect ")

m=Mobile("iPhone")
charge=Charger(" iPhone charger")

print(m.mname)
m.hasmobile(charge)
print(m.C1.cname)       
m. C1. getcharger()
print(charge. cname)
charge. getcharger()




print("***********************")
class Charger:
    def __init__(self, name):
        self.cname=name
        print("charger is ready")
    def getcharger(self):
        print(" charger is ready to connect ")

class Mobile:
    def __init__(self,name):
        self. mname=name
        self.C1=""    
        print("mobile is ready")  
        
    def hasmobile(self,c):
        self.C1=c
        print(" both are ready to connect ")

m=Mobile("iPhone")
charge=Charger(" iPhone charger")

print(m.mname)
m.hasmobile(charge)
print(m.C1.cname)       
m. C1. getcharger()

del m
print(charge. cname)
charge. getcharger()