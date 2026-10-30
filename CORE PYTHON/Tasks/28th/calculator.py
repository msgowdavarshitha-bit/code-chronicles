class Calculator:

    # Instance methods are add and subtract
    def add(self, a, b):
        print("Addition:", a + b)



    def subtract(self, a, b):
        print("Subtraction:", a - b)



    # Static methods multiply and divide
    @staticmethod    #i used the decorator to declare it as a static method 
    def multiply(a, b):
        print("Multiplication:", a * b)

    # Static method
    @staticmethod
    def divide(a, b):
        if b != 0:
            print("Division:", a / b)
        else:
            print("Cannot divide by zero")

    @staticmethod
    def floor_divide(a, b):   #as per the  Arithmetic operators i included floor division for the non decimal remainder 

        if b != 0:
            print("Division:", a // b)
        else:
            print("Cannot divide by zero")

    #in the same way we can use all the remaining operator 
c1 = Calculator()

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))


c1.add(a, b)
c1.subtract(a, b)


c1.multiply(a, b)
c1.divide(a, b)
c1.floor_divide(a, b)