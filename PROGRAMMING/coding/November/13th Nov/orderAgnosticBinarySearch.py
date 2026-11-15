print("Order agnostic binary search")
print("Means that the algorithm identifies it as a ascending or a descending and then performs binary search")
print("Normal binary search assumes that given array is in ascending order")

def intArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter the element: "))
            l1.append(n)
        except Exception as e:
            return l1

def orderAgnosticBinarySearch(arr,target):
    start,end=0,len(arr)-1

    #check whether array is in ascending or descending order
    #probability check
    flag="asc"
    if arr[start]>arr[end]:
        flag="desc"

    while start<=end:
        mid=(start+end)//2

        if target==arr[mid]:
            return mid

        elif flag=="asc":
            if target<arr[mid]:
                end=mid-1
            else:
                start=mid+1
        else:
            if target<arr[mid]:
                start=mid+1
            else:
                end=mid-1


    return -1

arr=intArr()
target=int(input("Enter the element to be searched: "))

result=orderAgnosticBinarySearch(arr,target)

if result!=-1:
    print(target,"is found at the index",result)
else:
    print(target,"found not found")