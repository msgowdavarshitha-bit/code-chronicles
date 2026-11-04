
print("Reverse the array using the slicing")

def intArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter the element: "))
            l1.append(n)
        except Exception as e:
            return l1

def reverse_arr(arr):
    return arr[::-1]


arr=intArr()
print(arr)
reversed_array=reverse_arr(arr)   #since i returned store it in a variable and print it down
print("Reversed array using the reversed function along with type conversion as list logic 1",reversed_array)

#third m/m is created

#reversed() is a predefined function



# Reverse the array using the slicing
# Enter the element: 2
# Enter the element: 3
# Enter the element: 1
# Enter the element: 4
# Enter the element: -22
# Enter the element: 0
# Enter the element: 10
# Enter the element: 
# [2, 3, 1, 4, -22, 0, 10]
# Reversed array using the reversed function along with type conversion as list logic 1 [10, 0, -22, 4, 1, 3, 2]