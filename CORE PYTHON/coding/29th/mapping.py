print("Mapping function: ")

def operation(data):
    r=data+10
    return r
l=[2,3,5,1,6,9,8,7]

k=list(map(operation,l))
print(k)

# Mapping function: 
# [12, 13, 15, 11, 16, 19, 18, 17]