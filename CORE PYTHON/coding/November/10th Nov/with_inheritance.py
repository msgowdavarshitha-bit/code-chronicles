
print("Here all the classes having same methods/function with the same print() statements so use the inheritance concept")

class Plane:
    def fly(self):
            print(" plane is flying ")
    
    def land(self):
        print(" plane is landing")
    
    def takeoff(self):
        print(" plane is takeoff")
    
class CargoPlane(Plane):
    # def fly(self):
    #     print(" plane is flying ")

    # def land(self):
    #     print(" plane is landing")

    # def takeoff(self):
    #     print(" plane is takeoff")

    def carryC(self):
        print(" plane is carry cargo")




class PassengerPlane(Plane):
    # def fly(self):
    #     print(" plane is flying ")

    # def land(self):
    #     print(" plane is landing")

    # def takeoff(self):
    #     print(" plane is takeoff")

    def carryP(self):
        print(" plane is carry passenger")



class FighterPlane(Plane):
    # def fly(self):
    #     print(" plane is flying ")

    # def land(self):
    #     print(" plane is landing")

    # def takeoff(self):
    #     print(" plane is takeoff")

    def carryW(self):
        print(" plane is carry weapons")


c=CargoPlane()
p=PassengerPlane()

f=FighterPlane()

f.land()
p.fly()
c.takeoff()
f.carryW()

# Here all the classes having same methods/function with the same print() statements so use the inheritance concept
#  plane is landing
#  plane is flying 
#  plane is takeoff

#the adding the new feature to the existing features in the parent
#  plane is carry weapons



print("============================"*2)
print("When we want to use parent method within in the class instead of calling from outside")


class Plane:
    def fly(self):
            print(" plane is flying ")
    
    def land(self):
        print(" plane is landing")
    
    def takeoff(self):
        print(" plane is takeoff")
    
class CargoPlane(Plane):
    # def fly(self):
    #     print(" plane is flying ")

    # def land(self):
    #     print(" plane is landing")

    # def takeoff(self):
    #     print(" plane is takeoff")

    

    def carryC(self):
        print(" plane is carry cargo")
        Plane.fly(self)




class PassengerPlane(Plane):
    # def fly(self):
    #     print(" plane is flying ")

    # def land(self):
    #     print(" plane is landing")

    # def takeoff(self):
    #     print(" plane is takeoff")

    def carryP(self):
        print(" plane is carry passenger")



class FighterPlane(Plane):
    # def fly(self):
    #     print(" plane is flying ")

    # def land(self):
    #     print(" plane is landing")

    # def takeoff(self):
    #     print(" plane is takeoff")

    def carryW(self):
        print(" plane is carry weapons")


c=CargoPlane()
p=PassengerPlane()

f=FighterPlane()

f.land()
p.fly()
c.takeoff()
f.carryW()









print("============================"*2)
print("When we want to use parent method within in the class instead of calling from outside")


class Plane:
    def fly(self):
            print(" plane is flying ")
    
    def land(self):
        print(" plane is landing")
    
    def takeoff(self):
        print(" plane is takeoff")
    
class CargoPlane(Plane):
    # def fly(self):
    #     print(" plane is flying ")

    # def land(self):
    #     print(" plane is landing")

    # def takeoff(self):
    #     print(" plane is takeoff")

    

    def carryC(self):
        print(" plane is carry cargo")
        Plane.fly(self)




class PassengerPlane(Plane):
    # def fly(self):
    #     print(" plane is flying ")

    # def land(self):
    #     print(" plane is landing")

    # def takeoff(self):
    #     print(" plane is takeoff")

    def carryP(self):
        print(" plane is carry passenger")



class FighterPlane(Plane):
    # def fly(self):
    #     print(" plane is flying ")

    # def land(self):
    #     print(" plane is landing")

    # def takeoff(self):
    #     print(" plane is takeoff")

    def carryW(self):
        print(" plane is carry weapons")


c=CargoPlane()
p=PassengerPlane()

f=FighterPlane()

f.land()
p.fly()
c.takeoff()
f.carryW()
f.fly()
f.takeoff()
p.land()
p.takeoff()
c.land()
c.fly()

