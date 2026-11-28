def intArr():
    l1=[]
    while True:
        try:
            l1.append(int(input("ENter the elements: ")))
        except Exception as e:
            return l1

def segregation(arr):
    dict={}
    for i in range(0,len(arr)):
        if arr[i] in dict:
            dict[arr[i]]=dict[arr[i]]+1
        else:
            dict[arr[i]]=1

    dup,non_dup,unique=[],[],[]

    for key,val in dict.items():
        if val>1:
            dup.append(key)
        elif val==1:
            unique.append(key)
    non_dup=dup+unique

    return dup,non_dup,unique


print("enter the element in to the array:")
arr=intArr()
print("created array:",arr)
resdup, resnondup, resunique = segregation(arr)
print("duplicates:",resdup)
print("non duplicates:",resnondup)
print("unique:",resunique)


print("get() is a method that returns the value of the key if present and if not present it will default return None, we can also customize the default value")

print("Using get() method")

def intArr():
    l1=[]
    while True:
        try:
            l1.append(int(input("ENter the elements: ")))
        except Exception as e:
            return l1

def segregation(arr):
    dict={}
    for i in range(0,len(arr)):
        dict[arr[i]]=dict.get(arr[i],0)+1

    dup,non_dup,unique=[],[],[]

    for key,val in dict.items():
        if val>1:
            dup.append(key)
        elif val==1:
            unique.append(key)
    non_dup=dup+unique

    return dup,non_dup,unique


print("enter the element in to the array:")
arr=intArr()
print("created array:",arr)
resdup, resnondup, resunique = segregation(arr)
print("duplicates:",resdup)
print("non duplicates:",resnondup)
print("unique:",resunique)