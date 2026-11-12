def intArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter the element: "))
            l1.append(n)
        except Exception as e:
            return l1

def mergeSrt(arr,start,mid,end):
    i,j=0,mid+1
    l1=[]

    for i in range(0,end-start+1):
        if i<=mid and j<=mid:
            if arr[i]>arr[j]:
                l1.append(arr[i])
                i+=1
            else:
                l1.append(arr[j])
                j+=1
        else:
            if i<=mid:
                l1.append(arr[i])
                i+=1
            else:
                l1.append(arr[j])
                j+=1
    for k in range(0,len(l1)):
        arr[start]=l1[k]
        start+=1

def merge(arr,start,end):
    if start>=end:
        return
    mid=(start+end)//2

    merge(arr,start,mid)
    merge(arr,mid+1,end)
    mergeSrt(arr,start,mid,end)
    

arr=intArr()
merge(arr)
