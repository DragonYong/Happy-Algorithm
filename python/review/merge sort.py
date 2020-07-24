import numpy as np


def merge_sort(arrs):
    if len(arrs) < 2:
        return arrs

    middle = len(arrs)//2
    return merge(merge_sort(arrs[:middle]), merge_sort(arrs[middle:]))


def merge(arr1, arr2):
    result = []
    while arr1 and arr2:
        if arr1[0] < arr2[0]:
            result.append(arr1.pop(0))
        else:
            result.append(arr2.pop(0))
    while arr1:
        result.append(arr1.pop(0))
    while arr2:
        result.append(arr2.pop(0))

    return result


arr = np.random.randint(0, 100, 23)
arr = list(arr)
print(merge_sort(arr))
