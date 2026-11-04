print("Using the two pointer approach")
def intArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter the element: "))
            l1.append(n)
        except Exception as e:
            return l1


def reversed_arr(arr):
    i,j=0,len(arr)-1

    while i<j:
        arr[i],arr[j]=arr[j],arr[i]

        i+=1
        j-=1

arr=intArr()
print(arr)
reversed_arr(arr)
print("The reversed array using 2 pointers approach",arr)



# Using the two pointer approach
# Enter the element: 2
# Enter the element: 1
# Enter the element: 5
# Enter the element: -9
# Enter the element: 45
# Enter the element: 0
# Enter the element: 10
# Enter the element: 
# [2, 1, 5, -9, 45, 0, 10]
# The reversed array using 2 pointers approach [10, 0, 45, -9, 5, 1, 2]