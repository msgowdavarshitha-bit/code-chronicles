print("Filter() function")

#extracting particular elements from list of elements using the particular filter condition

def even(num):
    if num%2==0:
        return True
    else:
        return False

l=[]
i=0
while i<4:
    n=int(input("ENter: "))
    l.insert(i,n)
    i+=1

print("original list")
print(l)


print("Even numbers using the filter() function ")
k=list(filter(even,l))  # filter(function_name, list_name)
print(k)
