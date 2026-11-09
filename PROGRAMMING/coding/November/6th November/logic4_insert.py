
def intArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter the element: "))
            l1.append(n)
        except Exception as e:
            return l1

def mergeLogic4(arr1,arr2):
    n=len(arr1)
    for i in arr2:
        arr1.insert(n,i)
        n+=1


arr1=intArr()
arr2=intArr()

print("Created array1 before merge: ",arr1)
print("Created array2 before merge: ",arr2)
print(id(arr1))
print(id(arr2))
mergeLogic4(arr1,arr2)
print("Created array1 after merge: ",arr1)
print(id(arr1))



# Enter the element: 2
# Enter the element: 6
# Enter the element: 
# Enter the element: 1
# Enter the element: 9
# Enter the element: 0
# Enter the element: 
# Created array1 before merge:  [2, 6]
# Created array2 before merge:  [1, 9, 0]
# 2887965507520
# 2887967335360
# Created array1 after merge:  [2, 6, 1, 9, 0]
# 2887965507520

