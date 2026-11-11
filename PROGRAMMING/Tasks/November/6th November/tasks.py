# Q1: merge alternately (arr1 first, then arr2); leftovers go at the end
def merge_alternate(arr1, arr2):
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        arr1.insert(i + 1, arr2[j])   # put arr2[j] right after arr1[i]
        i += 2
        j += 1
    while j < len(arr2):              # arr1 exhausted
        arr1.append(arr2[j])
        j += 1


# Q2: both ascending -> ascending
def merge_asc_asc_to_asc(arr1, arr2):
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr2[j] <= arr1[i]:
            arr1.insert(i, arr2[j])
            j += 1
        i += 1
    while j < len(arr2):
        arr1.append(arr2[j])
        j += 1


# Q4: both ascending -> descending (cursors at the end of each array)
def merge_asc_asc_to_desc(arr1, arr2):
    p, j = 0, len(arr2) - 1           # p = next result position at the front
    while p < len(arr1) and j >= 0:
        if arr1[-1] >= arr2[j]:       # largest unprocessed arr1 element is at the end
            arr1.insert(p, arr1.pop())
        else:
            arr1.insert(p, arr2[j])
            j -= 1
        p += 1
    while j >= 0:                     # arr1 finished, place the rest of arr2
        arr1.insert(p, arr2[j])
        p += 1
        j -= 1
    while p < len(arr1):              # arr2 finished, reverse the rest of arr1
        arr1.insert(p, arr1.pop())
        p += 1


# Q5: both descending -> descending (cursors at the end of each array)
def merge_desc_desc_to_desc(arr1, arr2):
    m, j = len(arr1), len(arr2) - 1   # m = count of unprocessed arr1 elements
    while m > 0 and j >= 0:
        if arr1[m - 1] <= arr2[j]:    # smaller one belongs at the back
            m -= 1                    # arr1's element is already in place
        else:
            arr1.insert(m, arr2[j])   # put arr2's smaller element just after arr1's unprocessed part
            j -= 1
    while j >= 0:                     # arr1 finished, rest of arr2 goes in front
        arr1.insert(m, arr2[j])
        j -= 1


# Q6: both descending -> ascending (cursors at the end of each array)
def merge_desc_desc_to_asc(arr1, arr2):
    p, j = 0, len(arr2) - 1
    while p < len(arr1) and j >= 0:
        if arr1[-1] <= arr2[j]:       # smallest unprocessed arr1 element is at the end
            arr1.insert(p, arr1.pop())
        else:
            arr1.insert(p, arr2[j])
            j -= 1
        p += 1
    while j >= 0:
        arr1.insert(p, arr2[j])
        p += 1
        j -= 1
    while p < len(arr1):
        arr1.insert(p, arr1.pop())
        p += 1


# Q7: arr1 ascending, arr2 descending -> ascending
def merge_asc_desc_to_asc(arr1, arr2):
    i, j = 0, len(arr2) - 1           # arr1 smallest is at the front, arr2 smallest at the end
    while i < len(arr1) and j >= 0:
        if arr2[j] <= arr1[i]:
            arr1.insert(i, arr2[j])
            j -= 1
        i += 1
    while j >= 0:
        arr1.append(arr2[j])
        j -= 1


# Q8: arr1 descending, arr2 ascending -> descending
def merge_desc_asc_to_desc(arr1, arr2):
    i, j = 0, len(arr2) - 1           # arr1 largest is at the front, arr2 largest at the end
    while i < len(arr1) and j >= 0:
        if arr2[j] >= arr1[i]:
            arr1.insert(i, arr2[j])
            j -= 1
        i += 1
    while j >= 0:
        arr1.append(arr2[j])
        j -= 1


# ---- tests ----
tests = [
    (merge_alternate,          [45, 67, 45, 82], [1, 2, 3, 4, 5, 3, 4, 2, 2]),
    (merge_alternate,          [45, 67, 45, 82], [100]),
    (merge_alternate,          [], []),
    (merge_alternate,          [45, 67, 1], [1, 2, 3]),
    (merge_asc_asc_to_asc,     [-3, -3, 0, 9, 10], [0, 1, 2, 3, 4, 5, 6, 7, 8, 11]),
    (merge_asc_asc_to_desc,    [0, 1, 9, 12], [10, 19, 100]),
    (merge_desc_desc_to_desc,  [10, 9, 1, -1], [100, 19, 10]),
    (merge_desc_desc_to_asc,   [10, 9, 1, -1], [100, 19, 10]),
    (merge_asc_desc_to_asc,    [-1, 1, 9, 10], [100, 19, 10]),
    (merge_desc_asc_to_desc,   [10, 9, 1, -1], [10, 19, 100]),
]
for fn, a, b in tests:
    fn(a, b)
    print(fn.__name__, a)