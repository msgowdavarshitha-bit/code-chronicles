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
    j=0
    for i in range(len(arr1),len(arr1)+len(arr2)):
        arr1.append(arr2[j])
    # return arr1


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