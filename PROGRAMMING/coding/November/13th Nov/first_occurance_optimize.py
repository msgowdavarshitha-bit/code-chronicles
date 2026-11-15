def intArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter the element: "))
            l1.append(n)
        except Exception as e:
            return l1

def firstOcc(arr,target):
    start,end=0,len(arr)-1
    first_occ=-1

    while start<=end:
        mid=(start+end)//2
        if target<=arr[mid]:
            if target==arr[mid]:
                first_occ=mid
                end=mid-1
        else:
            start=mid+1
    return first_occ


arr=intArr()
target=int(input("Enter the target element: "))

result=firstOcc(arr,target)

if result!=-1:
    print("First occurence of",target,"is found at",result)
else:
    print(target,"Not found")