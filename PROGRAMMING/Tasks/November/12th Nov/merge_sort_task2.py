
#Q4
#WAP to merge the given 2 ascending sorted array in descending order
# keep cursor at the end of each array
#arr1=[0,1,9,12] 
#arr2=[10,19,100]
#result=[100,19,12,10,1,0]



def intArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter the elements: "))
            l1.append(n)
        except Exception as e:
            return l1

def mergeSort(arr1,arr2):
    i,j=0,0
    res=[]
    n1,n2=len(arr1),len(arr2)
    for k in range(0,(n1+n2)):
        if i<n1 and j<n2:
            if arr1[i]>arr2[j]:
                res.append(arr1[i])
                i-=1
            else:
                res.append(arr2[j])
                j-=1

        else:
            if i<n1:
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
