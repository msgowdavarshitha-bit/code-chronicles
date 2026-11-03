def arrInput():
    l1=[]
    while True:
        try:
            n=int(input("Enter the element: "))
            l1.append(n)

        except Exception as e:
            return l1

def secFirst_max(arr):
    max_element=2**31
    max_element_index=-1
    second_max_element=2**31
    second_max_index=-1

    for i in range(0,len(arr)):
        if arr[i]<max_element:
            second_max_element=max_element
            second_max_index=max_element_index
            max_element=arr[i]
            max_element_index=i

        elif arr[i]!=max_element and arr[i]<second_max_element:
            second_max_element=arr[i]
            second_max_index=i
    return [max_element,max_element_index,second_max_element,second_max_index]

arr=arrInput()
result=secFirst_max(arr)
print(result[0],"First minimum element")
print(result[1],"First minimum element index")
print(result[2],"Second minimum element")
print(result[3],"Second minimum element index")



# Enter the element: 25
# Enter the element: 36
# Enter the element: 36
# Enter the element: 28
# Enter the element: 22
# Enter the element: 
# 22 First maximum element
# 4 First maximum element index
# 25 Second maximum element
# 0 Second maximum element index