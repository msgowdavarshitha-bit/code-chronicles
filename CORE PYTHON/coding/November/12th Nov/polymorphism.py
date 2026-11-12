class Plane:
    def takeoff(self):
        print("Plane is takeoff")
    def land(self):
        print("Plane is takeoff")

class Cargo(Plane):
    def takeoff(self):
        print("Cargo is takeoff")
    def land(self):
        print("Cargo is takeoff")

class Passenger(Plane):
    def takeoff(self):
        print("Passenger is takeoff")
    def land(self):
        print("Passenger is takeoff")

class Fighter(Plane):
    def takeoff(self):
        print("Fighter is takeoff")
    def land(self):
        print("Fighter is takeoff")

C=Cargo()
P=Passenger()
F=Fighter()



#instead of using reference and method name multiple times declare one function by passing the reference variable 
# and call the reference_variable.method

def allowPlane(ref):
    ref.takeoff()
    ref.land()



#while allowing or using the particular child class just call the common function_name(Reference_variable_of_particular_child_class
allowPlane(C)
allowPlane(P)
allowPlane(F)

