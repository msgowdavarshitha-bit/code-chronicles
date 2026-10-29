#Mapping is used when we want to perform the specific operation on each element of the list and update it in a new list



def operation(n):
    n=n**2
    return n


l=[2,4,1,9,3,55,10]  #if not given a list take the elements form the users as written earlier

b=list(map(operation,l))    #use list bcz we want to convert it into a new list
print(b)