# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    # 1. outer loop, variable "i" goes from range 0 to the second to last item in the list
    for i in range(0, len(arr) - 1):
        # 2. inside the loop: set smallest item is equal to i
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # 3. for inner loop, iterate through the entire unsorted part of the list
        # or i+1 through length of arr
        for j in range(i + 1, len(arr)):
            # 4. comparison to find the smallest item
            if arr[j] < arr[smallest_index]:
                # 5. save the index of the smallest item
                smallest_index = j
        # TO-DO: swap
        if smallest_index != i:
            # 6. swap the item into place
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
# outer loop: i = 0 to n-1
#     inner loop: j = 0 to n-1-i
def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1 - i):
            # inside the inner loop, compare the item with the item on its right
            # if the left item is larger than the right item
            # then swap places
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
