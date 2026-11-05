def intArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter the element: "))
            l1.append(n)
        except Exception as e:
            return l1

def reverseArr(arr,i,j):
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1

def rotateLHS(arr,k):
    n=len(arr)
    if k>=n:     #if the number of rotations are greater than a the number of elements that is len(array)   convert the cycles to the remainder of rotations % len(arr)
        k=k%n
    #step 1
    reverseArr(arr,0,(n-1))
    
    #step 2
    reverseArr(arr,k,(n-1))

    #step 3
    reverseArr(arr,0,(k-1))
    



arr=intArr()
print("The array before rotation",arr)
k=int(input("Enter the number of rotations you need: "))
rotateLHS(arr,k)
print("The array after rotation",arr)

