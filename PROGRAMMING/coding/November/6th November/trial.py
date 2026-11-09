# # def intArr():
# #     l1=[]
# #     while True:
# #         try:
# #             n=int(input("Enter the element: "))
# #             l1.append(n)
# #         except Exception as e:
# #             return l1


# def mergeArr(arr1,arr2):
#     n1=len(arr1)
#     n2=len(arr2)
#     i,j=0,0

#     while i<len(arr1):
#         if j<len(arr2):
#             arr1.insert(i,arr2[i])
#             i+=2
#             j+=1
#         else:
#             break
#         while j<len(arr2):
#             arr1.insert(i,arr2[j])
#             j+=1

# # arr1=intArr()
# # arr2=intArr()
# arr1=[21,32,45]
# arr2=[1,21,21,35,82,99]
# mergeArr(arr1,arr2)
# print(arr1)




# def mergeArr(arr1, arr2):
#     i, j = 0, 0

#     while i < len(arr1) and j < len(arr2):
#         arr1.insert(i, arr2[j])
#         i += 2
#         j += 1

#     # arr1 is exhausted, so append whatever is left of arr2
#     while j < len(arr2):
#         arr1.insert(i, arr2[j])
#         i += 1
#         j += 1


# arr1 = [21, 32, 45]
# arr2 = [1, 21, 21, 35, 82, 99]
# mergeArr(arr1, arr2)
# print(arr1)


def mergeArr(arr1, arr2):
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr2[j] <= arr1[i]:
            arr1.insert(i, arr2[j])   # arr2 element is smaller, so it goes before arr1[i]
            j += 1
        i += 1                        # move forward by 1, not 2

    # arr1 is exhausted, so the rest of arr2 is larger than everything in arr1
    while j < len(arr2):
        arr1.insert(i, arr2[j])
        i += 1
        j += 1


arr1 = [21, 32, 45]
arr2 = [1, 21, 21, 35, 82, 99]
mergeArr(arr1, arr2)
print(arr1)