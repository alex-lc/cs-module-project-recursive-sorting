# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    merged_arr = []

    # while there is more than one element in each array
    # compare the 0th index values to determine which is smaller
    # add that value to the merged array, replacing the correct index
    a_idx = 0
    b_idx = 0

    while a_idx < len(arrA) and b_idx < len(arrB):
        if arrA[a_idx] < arrB[b_idx]:
            # merged_arr[a_idx] = arrA[a_idx]
            merged_arr.append(arrA[a_idx])
            a_idx += 1
        else:
            # merged_arr[a_idx] = arrB[b_idx]
            merged_arr.append(arrB[b_idx])
            b_idx += 1

    if a_idx == len(arrA):
        merged_arr.extend(arrB[b_idx:])
    else:
        merged_arr.extend(arrA[a_idx:])

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    midpoint = len(arr) // 2
    left = arr[:midpoint]
    right = arr[midpoint:]

    # base case
    if len(left) < 2 and len(right) < 2:
        return merge(left, right)
    else:
        return merge(merge_sort(left), merge_sort(right))

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
