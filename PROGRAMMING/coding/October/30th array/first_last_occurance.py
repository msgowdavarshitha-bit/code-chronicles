def intArr():
    arr1=[]
    while True:
        try:
            n=int(input("ENter: "))
            arr1.append(n)
        except Exception as e:
            return arr1


result=[-1,-1]
arr=intArr()
target=int(input("ENter the target: "))

for i in range(0,len(arr)):
    if target==arr[i]:
        if result[0]!=-1:
            result[1]=i
        else:
            result[0]=i
            result[1]=i

print(result)
