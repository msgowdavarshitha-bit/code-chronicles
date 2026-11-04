print("INSERTION SORT")
print("Insertion sort descending order")
#We have not to return anything because it is in the place


def intArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter the element: "))
            l1.append(n)
        except Exception as e:
            return l1



def insertion_sort(arr):
    n=len(arr)
    for i in range(0,n-1):
        for j in range((i+1),1-1,-1):
            if arr[j-1]<arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]

arr=intArr()
insertion_sort(arr)
print(arr)




# INSERTION SORT
# Insertion sort descending order
# Enter the element: 2
# Enter the element: 1
# Enter the element: 3
# Enter the element: 4
# Enter the element: 5
# Enter the element: 10
# Enter the element: 
# [10, 5, 4, 3, 2, 1]