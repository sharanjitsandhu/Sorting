# ** Recursive func breaks the problem down into smaller problems
# and call itself for each of the smaller problems. eg. factorial **

# TO-DO: complete the helper function below to merge 2 sorted arrays


def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    # TO-DO
    merged_arr = []
    i = 0
    j = 0
    while i < len(arrA) and j < len(arrB):
        if arrB[j] > arrA[i]:
            merged_arr.append(arrA[i])
            i += 1
        else:
            merged_arr.append(arrB[j])
            j += 1
    while i < len(arrA):
        merged_arr.append(arrA[i])
        i += 1
    while j < len(arrB):
        merged_arr.append(arrB[j])
        j += 1

    return merged_arr


# Merge Sort is recursive(method that calls itself)
# Divide-and-Conquer algo
# very efficient for large data sets
# Merge sort does log n merge steps because each merge step doubles the list size
# It does n work for each merge step beacause it must look at every item
# So, it runs in O(n log n)

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
        # TO-DO
    if len(arr) <= 1:
        return arr
    halfway_index = len(arr) // 2

    left = merge_sort(arr[:halfway_index])
    right = merge_sort(arr[halfway_index:])
    arr = merge(left, right)
    return arr

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
