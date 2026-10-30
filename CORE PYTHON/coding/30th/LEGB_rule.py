from math import pi as a    #Built-in scope

a=10    #global scope

def outer():
    a=200     #Enclosed scope

    def inner():

        a=700     #local scope
        print(a)
    inner()

outer()