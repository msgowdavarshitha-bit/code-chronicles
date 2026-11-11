print("Without inheritance")

print("If the methods and code/logic and statements are same for all the classes use the inheritance or else dont use inheritance just use the normal class methodes/ functions")

class CargoPlane:
    def fly(self):
        print("Cargo plane is flying ")

    def land(self):
        print("Cargo plane is landing")

    def takeoff(self):
        print("Cargo plane is takeoff")

    def carry(self):
        print("Cargo plane is carry cargo")




class PassengerPlane:
    def fly(self):
        print("passenger plane is flying ")

    def land(self):
        print("passenger plane is landing")

    def takeoff(self):
        print("passenger plane is takeoff")

    def carryP(self):
        print("passenger plane is carry passenger")



class FighterPlane:
    def fly(self):
        print("Fighter plane is flying ")

    def land(self):
        print("Fighter plane is landing")

    def takeoff(self):
        print("Fighter plane is takeoff")

    def carryW(self):
        print("Fighter plane is carry weapons")


c=CargoPlane()
p=PassengerPlane()

f=FighterPlane()

f.land()
p.fly()
c.takeoff()



print()
print("========================="*2)

print("Here all the classes having same methods/function with the same print() statements so use the inheritance concept")
class CargoPlane:
    def fly(self):
        print(" plane is flying ")

    def land(self):
        print(" plane is landing")

    def takeoff(self):
        print(" plane is takeoff")

    def carry(self):
        print(" plane is carry cargo")




class PassengerPlane:
    def fly(self):
        print(" plane is flying ")

    def land(self):
        print(" plane is landing")

    def takeoff(self):
        print(" plane is takeoff")

    def carryP(self):
        print(" plane is carry passenger")



class FighterPlane:
    def fly(self):
        print(" plane is flying ")

    def land(self):
        print(" plane is landing")

    def takeoff(self):
        print(" plane is takeoff")

    def carryW(self):
        print(" plane is carry weapons")


c=CargoPlane()
p=PassengerPlane()

f=FighterPlane()

f.land()
p.fly()
c.takeoff()

