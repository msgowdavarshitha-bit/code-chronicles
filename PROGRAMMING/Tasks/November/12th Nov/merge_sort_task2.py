#Q2
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
    n1,n2=len(arr1),len(arr2)
    i,j=n1-1,n2-1
    res=[]
    while i>=0 and j>=0:
        if arr1[i]>arr2[j]:
            res.append(arr1[i])
            i-=1
        else:
            res.append(arr2[j])
            j-=1

    
    while i>=0:
        res.append(arr1[i])
        i-=1
    while j>=0:
        res.append(arr2[j])
        j-=1
    return res

arr1=intArr()
arr2=intArr()
result=mergeSort(arr1,arr2)
print(result)
