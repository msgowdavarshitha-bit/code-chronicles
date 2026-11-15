
def intArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter the element: "))
            l1.append(n)
        except ValueError:
            return l1


def mountain_array(arr):
    start,end=0,len(arr)-1

    while start<end:
        mid=(start+end)//2

        if arr[mid]<arr[mid+1]:
            start=mid+1
        else:
            end=mid

    return start


arr=intArr()

if arr:
    result=mountain_array(arr)
    print(arr[result],"is the peak element found at",result)
else:
    print("Array is empty")
