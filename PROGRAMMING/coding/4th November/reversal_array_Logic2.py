print("Logic 2")


print("Reverse the array using the 3rd variable and using reversed pre defined function along with type conversion")

def intArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter the element: "))
            l1.append(n)
        except Exception as e:
            return l1

def reverse_arr(arr):
    return list(reversed(arr))
arr=intArr()
print(arr)
reversed_array=reverse_arr(arr)   #since i returned store it in a variable and print it down
print("Reversed array using the reversed function along with type conversion as list logic 2",reversed_array)

#third m/m is created

#reversed() is a predefined function which will convert the array into a reversed array



# Logic 2
# Reverse the array using the 3rd variable and using reversed pre defined function along with type conversion
# Enter the element: 3
# Enter the element: 1
# Enter the element: 2
# Enter the element: 10
# Enter the element: -19
# Enter the element: -2
# Enter the element: 0
# Enter the element: 8
# Enter the element: 
# [3, 1, 2, 10, -19, -2, 0, 8]
# Reversed array using the reversed function along with type conversion as list logic 2 [8, 0, -2, -19, 10, 2, 1, 3]