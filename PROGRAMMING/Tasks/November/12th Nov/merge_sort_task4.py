#Q4
#WAP to merge the given 2 descending sorted array in ascending order
# keep cursor at the end of each array
#arr1=[10,9,1,-1] 
#arr2=[100,19,10]
#result=[-1,1,9,10,10,19,100]

def intArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter the element: "))
            l1.append(n)
        except Exception as e:
            return l1


def mergeSort(arr1,arr2):
    n1,n2=len(arr1),len(arr2)
    i,j=len(arr1)-1,len(arr2)-1
    res=[]

    for k in range(0,(n1+n2)):
        if i>=0 and j>=0:
            if arr1[i]<arr2[j]:
                res.append(arr1[i])
                i-=1
            else:
                res.append(arr2[j])
                j-=1
        elif i>=0:
            
            res.append(arr1[i])
            i-=1
        else:
            res.append(arr2[j])
            j-=1
    return res
arr1=intArr()
arr2=intArr()
result=mergeSort(arr1,arr2)
print(result)