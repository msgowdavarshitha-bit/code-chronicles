print("SELECTION SORT")

print("WAP to program to sort array in incrementing order")
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
        current_max_element,current_max_index=fineElem(a)   #if we want to using the function to sort but use the swap directly no need of j loop 
        # for j in range(0,n-i):
        #     if a[j]>current_max_element:
        #         current_max_element=a[j]
        #         current_max_index=j
        a[actual_end],a[current_max_index]=a[current_max_index],a[actual_end]



            

def fineElem(l1):
    max_element=l1[0]
    max_element_index=0
    for i in range(0,len(l1)):
        if l1[i]>max_element:
            max_element=l1[i]
            max_element_index=i
    return max_element,max_element_index



a=int_arr()
selectionSort(a)
print("NEW",a)



