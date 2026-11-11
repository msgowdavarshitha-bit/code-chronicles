print("Merge sort descending")

#Take the user i/p integer array
def intArr():
    l1 = []
    while True:
        try:
            n = int(input("Enter the element: "))
            l1.append(n)
        except ValueError:      
            return l1


# Merge arr[start..mid] and arr[mid+1..end] using a temp list
def mergeSortMerging(arr, start, mid, end):

    i, j = start, mid + 1
    res = []

    for k in range(0,end - start + 1):
        if i <= mid and j <= end:
            if arr[i] >= arr[j]:
                res.append(arr[i])
                i += 1
            else:
                res.append(arr[j])
                j += 1
        else:
            # one half is exhausted, copy the remaining values
            if i <= mid:
                res.append(arr[i])
                i += 1
            else:
                res.append(arr[j])
                j += 1

    # update the original array with the result array
    for k in range(0,len(res)):
        arr[start] = res[k]
        start += 1


# Divide the array
def mergeDivision(arr, start, end):
    # base condition: 0 or 1 element
    if start >= end:
        return

    mid = (start + end) // 2

    mergeDivision(arr, start, mid)        # left half
    mergeDivision(arr, mid + 1, end)      # right half
    mergeSortMerging(arr, start, mid, end)  # merge both halves


arr = intArr()
print("Un-Sorted array: ", arr)
mergeDivision(arr, 0, len(arr) - 1)
print("Sorted array: ", arr)