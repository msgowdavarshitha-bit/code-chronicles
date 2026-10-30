def add(a,b):
    r=a+b
    return r


result=add(10,40)
print(result)


#Instead all of these we can use lambda function

#Syntax:-  lambda arguments(n number of arguments can be passed based on the requirement) : expression (single expression can be passed)

res=lambda a,b:a+b
print(res(10,40))   #It is very important to pass the arguments value while calling the variable that holding lambda