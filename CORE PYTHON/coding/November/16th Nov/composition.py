print("Composition")
print("Without main object other objects cannot servive is called composed objects and the process is called as composition")

class OS:
    def __init__(self):
        self.status=True
        print("OS is installing")
        print("Os is still installing")

    def getOs(self):
        print("OS is installed")


class Mobile:
    def __init__(self,name):
        self.mname=name
        self.O=OS()

        print("Mobile is created")
        print("With OS is installed")

m=Mobile("Iphone")
print(m.mname)
print(m.O.status)

m.O.getOs()

print(m.O.status)



print("==========================================================================================")
#Implementation


class OS:
    def __init__(self):
        self.status=True
        print("OS is installing")
        print("Os is still installing")

    def getOs(self):
        print("OS is installed")


class Mobile:
    def __init__(self,name):
        self.mname=name
        self.O=OS()

        print("Mobile is created")
        print("With OS is installed")

m=Mobile("Iphone")
print(m.mname)
print(m.O.status)

m.O.getOs()
del m

#print(m.O.status)  NameError: name 'm' is not defined