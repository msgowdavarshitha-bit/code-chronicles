print("SELECTION SORT")

print("WAP to program to sort array in decrementing order")
def int_arr():
    arr=[]
    while True:
        try:
            n=int(input("Enter the element: "))
            arr.append(n)
        except Exception as e:
            return arr

def selectionSort(a):
    n=len(a)
    for i in range(0,n-1):
        actual_end=n-1-i
        current_min_element,current_min_index=2 ** 31, -1   #if we want to using the function to sort but use the swap directly no need of j loop 
        for j in range(0,n-i):
            if a[j]<current_min_element:
                current_min_element=a[j]
                current_min_index=j
        a[actual_end],a[current_min_index]=a[current_min_index],a[actual_end]



            

# def fineElem(l1):
#     max_element=-2**31
#     max_element_index=-1
#     for i in range(0,len(l1)):
#         if l1[i]>max_element:
#             max_element=l1[i]
#             max_element_index=i
#     return max_element,max_element_index



a=int_arr()
selectionSort(a)
print("NEW",a)


# SELECTION SORT
# WAP to program to sort array in decrementing order
# Enter the element: 3
# Enter the element: 1
# Enter the element: 4
# Enter the element: 2
# Enter the element: 5
# Enter the element: 0
# Enter the element: -1
# Enter the element: -5
# Enter the element: 
# NEW [5, 4, 3, 2, 1, 0, -1, -5]
