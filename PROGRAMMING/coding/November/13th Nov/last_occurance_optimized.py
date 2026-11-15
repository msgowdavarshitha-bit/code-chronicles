def intArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter the element: "))
            l1.append(n)
        except Exception as e:
            return l1


def lastOcc(arr,target):
    start,end=0,len(arr)-1
    last_occ=-1

    while start<=end:
        mid=(start+end)//2

        if target>=arr[mid]:
            if target==arr[mid]:
                last_occ=mid
            start=mid+1
        else:
            end=mid-1

    return last_occ

arr=intArr()
target=int(input("Enter the target element: "))

result=lastOcc(arr,target)
if result!=-1:
    print(target,"last occurence found at the index",result)
else:
    print(target,"Not found")
