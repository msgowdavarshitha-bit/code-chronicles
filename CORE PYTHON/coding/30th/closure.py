#Calling the inner function in the or the outside the outer function


def outer():
    print("Entering outer")
    print("processing")

    def inner():
        print("Entering outer")
        print("processing")
        print("Leaving inner")
    return inner

print("Program started")
print("calling ")

ref=outer()
print("Leaving outer")
print("INner function")
ref()
print("End")