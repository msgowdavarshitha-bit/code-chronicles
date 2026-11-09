def outer():

    print("ENtering outer function")

    def inner():
        print("Entering the function")
        print("Processing")
        print("Calling inner")
    inner()


outer()

#We cannot call the inner function outside the outer function 

#outer() call
#outer execute
#inner() call
#inner execute
