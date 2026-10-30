print(" Lambda is predefined function which is ananymous function that is present inside function and executed only once")

print("Program to print square root of the number")

def square(num):
    n=num*num
    return n
k=square(5)
print(k)


print("Same using lambda function")

k=lambda num:num*num
print(k(5))



print("Adding 2 numbers: ")

l=lambda n1,n2:n1+n2   #==> single expression only and multiple arguments
a=l(10,20)
print(a)