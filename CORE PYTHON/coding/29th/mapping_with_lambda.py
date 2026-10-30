print("Mapping with lambda")


def operation(data):
    r=data+10
    return r
l=[2,3,5,1,6,9,8,7]

k=list(map(lambda data:data+10,l))  #pass lambda function as a function for the map
print(k)