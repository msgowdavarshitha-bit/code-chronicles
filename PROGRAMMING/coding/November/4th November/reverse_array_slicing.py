arr=[5,9,2,0,-8,10,-2,25]

print(arr[::-1])
print(arr[len(arr)-1:-1:-1])  #results an empty array

print(arr[-1:-len(arr)-1:-1])



# [25, -2, 10, -8, 0, 2, 9, 5]
# []
# [25, -2, 10, -8, 0, 2, 9, 5]