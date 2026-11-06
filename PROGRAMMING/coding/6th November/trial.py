def intArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter the element: "))
            l1.append(n)
        except Exception as e:
            return l1


def mergeArr(arr1,arr2):
    n1=len(arr1)
    n2=len(arr2)
    i,j=0,0

    while i<len(arr1):
        if j<len(arr2):
            arr1.insert(i,arr2[i])
            i+=2
            j+=1
        else:
            break
        while j<len(arr2):
            arr1.insert(i,arr2[j])
            j+=1

arr1=intArr()
arr2=intArr()
mergeArr(arr1,arr2)
print(arr1)
