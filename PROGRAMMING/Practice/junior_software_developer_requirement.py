def intArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter the element: "))
            l1.append(n)
        except Exception as e:
            return l1

def selectionSort(arr):
    n=len(arr)
    for i in range(0,n-1):
        actual_end=n-i-1
        current_max_ele=-2**31
        current_max_ele_index=-1
        for j in range(0,n-i-1):
            if arr[j]>current_max_ele:
                current_max_ele=arr[j]
                current_max_ele_index=j
        arr[actual_end],arr[current_max_ele_index]=arr[current_max_ele_index],arr[actual_end]


arr=intArr()
selectionSort(arr)
print(arr)