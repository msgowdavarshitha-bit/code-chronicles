def intArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter the element: "))
            l1.append(n)
        except Exception as e:
            return l1


def mountain_array(arr):
    start,end=0,len(arr)-1

    while start<=end:
        mid=(start+end)//2

        if mid>0 and mid<len(arr)-1:
            if arr[mid-1]<arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid-1]>arr[mid]>arr[mid+1]:
                end=mid-1
                
            elif arr[mid-1]<arr[mid]<arr[mid+1]:
                start=mid+1

        #if at the first then unlimited loop and doesn't run
        elif mid==0:
            start=mid+1

        else:
            end=mid-1


    return -1

arr=intArr()
result=mountain_array(arr)
print(arr[result],"is the peak element found at",result)

