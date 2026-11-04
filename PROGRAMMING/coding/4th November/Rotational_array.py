print("Rotational array")

print("Definition:- #On complete rotational cycle of the array means shift each element of the array towards left hand side to right hand side one by one.")

print("#types of rotation")
#1. Left rotation
#2. right rotation


#Write a program to rotate the given integer array for k number of times towards LHS in place(without 3rd memory)

#constraints :=-   1<=len(arr)<=10**5
#                  -10**31<=arr[i]<=10**31  (inputs)
#                   0<=k<=10**5    ()

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
    #step 1
    reverseArr(arr,0,(k-1))

    #step 2
    reverseArr(arr,k,(n-1))

    #step 3
    reverseArr(arr,0,(n-1))



arr=intArr()
print("The array before rotation",arr)
k=int(input("Enter the number of rotations you need: "))
rotateLHS(arr,k)
print("The array after rotation",arr)




# Enter the element: 1
# Enter the element: 2
# Enter the element: 3
# Enter the element: 4
# Enter the element: 5
# Enter the element: 
# The array before rotation [1, 2, 3, 4, 5]
# Enter the number of rotations you need: 2
# The array after rotation [3, 4, 5, 1, 2]