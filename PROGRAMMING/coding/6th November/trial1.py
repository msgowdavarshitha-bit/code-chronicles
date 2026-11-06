def intArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter the element: "))
            l1.append(n)
        except Exception as e:
            return l1


def mergeArr(arr1,arr2):
    i,j=0,0

    while j<len(arr2):
        if i<len(arr1):
            arr1.insert(i+1,arr2[j])
            i+=2
            # j+=1
        else:
            arr1.insert(i,arr2[j])
            i+=1
        j+=1
    


arr1=intArr()
arr2=intArr()
mergeArr(arr1,arr2)
print(arr1)

print("Correct this")