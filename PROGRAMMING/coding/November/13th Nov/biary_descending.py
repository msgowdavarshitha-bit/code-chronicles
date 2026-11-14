print("BINARY SEARCH")

def intArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter the element: "))
            l1.append(n)
        except Exception as e:
            return l1

def binarySearch(arr,target):
    start,end=0,len(arr)-1

    while start<=end:
        mid=(start+end)//2

        if target==arr[mid]:
            return mid
        elif target<arr[mid]:
            start=mid+1
        else:
            end=mid-1

    return -1

arr=intArr()
print("Un-Sorted array: ",arr)
target=int(input("ENter the element to be searched in the sorted array: "))
result=binarySearch(arr,target)

if result!=-1:
    print(target,"Is found in the index",result)
else:
    print(target,"Is available at the index",result)
