print("DECORATOR")
# adding functionality to the existing code without modifying the original code

#Execute the function written in the book 




def outer(func):
    print("Entering outer")

    def inner():
        print("Entering inner")
        print("Processing")
        ref=func
        a=ref().upper()
        print(a)
        print("Leaving inner")
    return inner



@outer
def greet():
    # print("Hi")
    n=input("Enter the string: ")
    return n
greet()