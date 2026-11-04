print("REVERSAL OF ARRAY")

print("LOgic 1")
print("Reverse the array using the 3rd variable and decrementing loop")

def intArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter the element: "))
            l1.append(n)
        except Exception as e:
            return l1

def reverse_arr(arr):
    result=[]     #third variable to store the each element
    for i in range(len(arr)-1,-1,-1):    #decrementing loop start form last index and go till 0th index
        result.append(arr[i])    #while going append each element to the result array
    return result    #since we have third variable store it in a variable

arr=intArr()
print(arr)
reversed_array=reverse_arr(arr)   #since i returned store it in a variable and print it down
print("Reversed array using the third memory logic 1",reversed_array)



# REVERSAL OF ARRAY
# LOgic 1
# Reverse the array using the 3rd variable and decrementing loop
# Enter the element: 10
# Enter the element: -10
# Enter the element: 2
# Enter the element: 0
# Enter the element: 9
# Enter the element: 89
# Enter the element: 3
# Enter the element: -4
# Enter the element: -1
# Enter the element: 
# [10, -10, 2, 0, 9, 89, 3, -4, -1]
# Reversed array using the third memory logic 1 [-1, -4, 3, 89, 9, 0, 2, -10, 10]