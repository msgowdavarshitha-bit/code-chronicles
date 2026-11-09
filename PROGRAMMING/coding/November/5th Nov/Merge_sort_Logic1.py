print("WAP to merge the given arrays one after the other")


def intArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter the element: "))
            l1.append(n)
        except Exception as e:
            return l1

def mergeLogic1(arr1,arr2):
    res=arr1+arr2
    return res


arr1=intArr()
arr2=intArr()

print("Created array1 before merge: ",arr1)
print("Created array2 before merge: ",arr2)
print(id(arr1))
print(id(arr2))
res=mergeLogic1(arr1,arr2)
print(res)
print(id(res))
print("Created array1 after merge: ",arr1)
print("Created array2 after merge: ",arr2)
print(id(arr1))
print(id(arr2))