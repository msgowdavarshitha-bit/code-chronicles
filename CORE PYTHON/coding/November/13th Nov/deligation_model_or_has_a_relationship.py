print("When class has a is-a relationship use --> Inheritance")
print("When class has a has-a relationship use -->  has-a relationship")

#types of Has-a-relationship
#1.Aggregation(aggregation object)
#2.Composition(Composition object)

class Radio:
    def turnon(self,x):
        if x==1:
            print("Radio is on")
        else:
            print("Radio is off")

class Car:
    def __init__(self,name):
        self.name=name
        self.r=Radio()

    def start(self):
        print("Engine started")

name=input("Enter the name of the car: ")
c=Car(name)

print(c.name)
c.r.turnon(1)
c.r.turnon(0)

c.start()


# Enter the name of the car: BMW
# BMW
# Radio is on
# Radio is off
# Engine started