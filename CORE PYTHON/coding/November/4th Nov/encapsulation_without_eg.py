class Book:
    def __init__(self,value):
        if value>0:
            self.pages=value


b1=Book(100)
print(b1.pages)
b1.pages=112
print(b1.pages)
b1.pages=100
print(b1.pages)
b1.pages=-100
print(b1.pages)
print(b1.pages)