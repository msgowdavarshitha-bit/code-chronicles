print("WAP to merge array one by one")

print("WAP to merge the given arrays one after the other")
print("Logic 3:- append()")

def intArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter the element: "))
            l1.append(n)
        except Exception as e:
            return l1

def mergeLogic1(arr1,arr2):
    for i in arr2:
        arr1.append(i)


arr1=intArr()
arr2=intArr()

print("Created array1 before merge: ",arr1)
print("Created array2 before merge: ",arr2)
print(id(arr1))
print(id(arr2))
mergeLogic1(arr1,arr2)

print("Created array1 after merge: ",arr1)
