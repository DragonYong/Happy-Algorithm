import numpy as np


def quick_sort(arr, left=None, right=None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr)-1 if not isinstance(right, (int, float)) else right
    if left < right:
        partition_index = partition(arr, left, right)
        quick_sort(arr, left, partition_index-1)
        quick_sort(arr, partition_index+1, right)

    return arr


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr, left, right):
    pivot = left
    index = pivot+1
    i = index
    while i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index += 1
        i += 1
    # 将标杆数据放到均等中间
    swap(arr, pivot, index-1)
    return index-1


arr = np.random.randint(0, 100, 20)
print("原始数据:", arr)

print("原始数据:", quick_sort(arr))
