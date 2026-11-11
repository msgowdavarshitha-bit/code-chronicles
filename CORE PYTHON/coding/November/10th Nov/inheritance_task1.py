class Animal:
    def sleep(self):
        print("It is sleeping")

    def eat(self):
        print("It is eating")

    def breath(self):
        print("It is breathing")


class Tiger(Animal):
    def tiger_eat(self):
        Animal.eat(self)

class Dog(Animal):
    pass

class Monkey(Animal):
    pass


t=Tiger()
d=Dog()
m=Monkey()

t.tiger_eat()