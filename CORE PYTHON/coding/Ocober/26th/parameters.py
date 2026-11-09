class Demo:
    def swap(self,x,y):   #Formal parameter which is in the function definition  that doesn't hold the value
        print(x,y)
        temp=x
        x=y
        y=temp

        print(x,y)
d1=Demo()
a=10
b=20

print(a,b)
d1.swap(a,b)   #Actual parameter which is in the function calling that holds the value
print(a,b)
