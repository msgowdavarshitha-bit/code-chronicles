def intArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter: "))
            l1.append(n)
        except Exception as e:
            return l1


def twoPointer(arr,target):
    i=0
    j=len(arr)-1

    res=[-1,-1]

    while i<=j:    #it is important take the while loop to go and stop where 
        if arr[i]==target and res[0]==-1:
            res[0]=i

        if arr[j]==target and res[1]==-1:
            res[1]=j

        i+=1
        j-=1

    return res


arr=intArr()
target=int(input("Enter the value you want to search: "))
a=twoPointer(arr,target)
print(a)