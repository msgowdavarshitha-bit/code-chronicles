class Demo:
    x=10

    def __init__(self):
        self.y=10
        self.z=20

    def instanceDis(self):
        print(self.x)
        print(self.y)
        self.a=13

    @staticmethod
    def staticDis():
        print(Demo.x)
        print()

    @classmethod
    def classDisp(cls):
        print("Dee")

d1=Demo()
d1.instanceDis()
Demo.staticDis()
Demo.classDisp()