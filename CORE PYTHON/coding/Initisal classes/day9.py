a=10
b=10
c=10

print(id(a))
print(id(b))
print(id(c))

print(a==b)
print(b==c)


e=292
f=234
g=292

print(e==f)
print(f==g)

#id is changing every time we execute a program



print("****"*10)

class Fan:
    def __init__(self):
        self.brand="N"
        self.color="w"
        self.price=2000
        print(self)
        print(id(self))
   

f1=Fan()
print(f1)
print(id(f1))
