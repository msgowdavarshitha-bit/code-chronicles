l=[2,3,4]


#passing lambda function as a function to filter()
a=list(filter(lambda n:n%2==0,l))



#passing lambda function as a function to mapping()
b=list(map(lambda n:n+25,l))

print(a)
print(b)