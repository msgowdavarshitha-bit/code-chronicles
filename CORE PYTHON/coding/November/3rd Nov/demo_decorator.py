def greet():
    print("Hi")


def outer(func):
    print("Entering outer")

    def inner():
        print("Entering inner")
        print("Processing")
        ref=func
        ref()
        print("Leaving inner")
    return inner

ptr1=greet   #returns the address of the greet
print(ptr1)

ptr2=outer(ptr1)
ptr2()