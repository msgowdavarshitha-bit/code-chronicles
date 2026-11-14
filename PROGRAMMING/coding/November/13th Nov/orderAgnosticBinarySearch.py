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

    peak=-1
    for i in range(0,len(arr)):
    
        mid=(start+end)//2
        if arr[mid-1]<arr[mid]>arr[mid+1]:
            peak=mid
        elif arr[mid-1]>arr[mid]>arr[mid+1]:
            start=mid+1
        elif arr[mid-1]<arr[mid]<arr[mid+1]:
            end=mid-1

    return -1

arr=intArr()
result=mountain_array(arr)
print(result)