#Q3
#WAP to merge the given 2 descending sorted array in descending order
# keep cursor at the end of each array
#arr1=[10,9,1,-1] 
#arr2=[100,19,10]
#result=[100,19,10,10,9,1,-1]


def intArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter the elements: "))
            l1.append(n)
        except Exception as e:
            return l1

def mergeSortDescending(arr1,arr2):
    i,j=0,0
    res=[]
    n1,n2=len(arr1),len(arr2)

    for k in range(0,(n1+n2)):
        if i<n1 and j<n2:
            if arr1[i]>arr2[j]:
                res.append(arr1[i])
                i+=1

            else:
                res.append(arr2[j])
                j+=1
        else:
            if i<n1:
                res.append(arr1[i])
                i+=1
            if j<n2:
                res.append(arr2[j])
                j+=1
    return res



arr1=intArr()
arr2=intArr()

result=mergeSortDescending(arr1,arr2)
print(result)


# Enter the elements: 10
# Enter the elements: 9
# Enter the elements: -1
# Enter the elements: 
# Enter the elements: 12
# Enter the elements: 2
# Enter the elements: 0
# Enter the elements: 
# [12, 10, 9, 2, 0, -1]