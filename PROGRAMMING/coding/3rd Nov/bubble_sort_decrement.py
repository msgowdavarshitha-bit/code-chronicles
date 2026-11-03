def arrInput():
    l1=[]
    while True:
        try:
            n=int(input("Enter the element: "))
            l1.append(n)

        except Exception as e:
            return l1


def bubble_sort(arr):
    n=len(arr)
    print("decrementing")
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    
arr=arrInput()
bubble_sort(arr)
print(arr)