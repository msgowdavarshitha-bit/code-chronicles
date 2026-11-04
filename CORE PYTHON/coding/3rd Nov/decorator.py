print("DECORATOR")
# adding functionality to the existing code without modifying the original code

#Execute the function written in the book

def outer(func):
    print("Entering outer")

    def inner():
        print("Entering inner")
        print("Processing")
        ref=func
        ref()
        print("Leaving inner")
    return inner



@outer      #decorator
def greet():
    print("Hi")
greet()