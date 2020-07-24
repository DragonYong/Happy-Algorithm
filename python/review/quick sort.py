import numpy as np


def quickSort(arr, left=None, right=None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr)-1 if not isinstance(right, (int, float)) else right
    if left < right:
        index = partition(arr, left, right)
        quickSort(arr, left, index-1)
        quickSort(arr, index+1, right)
    return arr


def partition(nums, left, right):
    # pivoit = 0
    # left = 0
    # right = len(nums)-1
    # counter = pivoit+1
    # i = counter
    # while i < right:
    #     if nums[i] < nums[pivoit]:
    #         swap(nums, i, counter)
    #         counter += 1
    #     i += 1
    # swap(nums, counter-1, pivoit)
    pivot = left
    index = pivot+1
    i = index
    while i <= right:
        if nums[i] < nums[pivot]:
            swap(nums, i, index)
            index += 1
        i += 1
    swap(nums, pivot, index-1)
    return index-1


def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]


nums = np.random.randint(0, 100, 40)
# nums = [3, 6, 2, 3, 4, 5, 1, 2, 3, 1, 0, 89, 64]
print(quickSort(nums))
